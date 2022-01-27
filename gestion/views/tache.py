from django.views.generic import TemplateView


class CreateTacheView(TemplateView):
    template_name = 'account/create-task.html'
    permissions = ['account.add_task']
    form_class = TaskForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(CreateTaskView, self).get_context_data(**kwargs)
        executor = self.request.user
        context['form'] = form if form else self.form_class()
        if not executor.is_administrator:
            context['form'].fields['assignation'].initial = executor
            context['form'].fields['assignation'].widget.attrs['disabled'] = 'true'
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        request = super(CreateTaskView, self).post(**kwargs)
        form = self.form_class(request.POST)
        context = self.get_context_data(form=form, **kwargs)
        if not form.is_valid():
            return self.render_to_response(context, status=400)
        # create the task
        try:
            task = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création de la tâche %s: %s' % (
                type(e).__name__, self.request.POST['object'], e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Tâche créé avec succès'
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, status=201)


class EditTaskView(BBandCoLoginRequiredMixin, BBandCoTemplateView):
    template_name = 'account/edit-task.html'
    permissions = ['account.change_task']
    form_class = TaskForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditTaskView, self).get_context_data(**kwargs)
        executor = self.request.user
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=task)
        if not executor.is_administrator:
            context['form'].fields['assignation'].widget.attrs['disabled'] = 'true'
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        request = super(EditTaskView, self).post(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, request.FILES, instance=task)
        context = self.get_context_data(form=form, **kwargs)
        if not form.is_valid():
            return self.render_to_response(context, status=400)
        # create the task
        try:
            task = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la modification de la tâche %s: %s' % (
                type(e).__name__, self.request.POST['object'], e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Tâche modifiée avec succès'
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, status=200)


class EditTaskStatusView(BBandCoLoginRequiredMixin, View):
    permissions = ['account.change_task']

    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.done = not task.done
        try:
            task.save()
            messages.add_message(request, messages.INFO, message='Tâche #%s mise à jour avec succès' % task.id)
        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 message='Erreur (%s) lors de la mise à jour de la tâche #%s : %s' % (
                                     type(e).__name__, task.id, e))
        return HttpResponseRedirect(reverse('account:task-my-list'))


class ListTaskView(BBandCoLoginRequiredMixin, BBandCoTemplateView):
    template_name = 'account/list-task.html'
    permissions = ['account.view_task']

    def get_context_data(self, *args, **kwargs):
        executor = self.request.user
        logger.debug('groups: %s' % executor.groups.filter(name='Administrateur').exists())
        if not executor.is_superuser or not executor.groups.filter(name='Administrateur').exists():
            raise PermissionDenied
        _lp = '[%s] %s.get_context_data' % (executor, self.__class__.__name__)
        context = super(ListTaskView, self).get_context_data(**kwargs)
        tasks = Task.objects.all()
        page_obj = self.get_paginated_list(tasks)
        context['page_obj'] = page_obj
        return context


class ListUserTaskView(BBandCoLoginRequiredMixin, BBandCoTemplateView):
    template_name = 'account/list-my-task.html'
    permissions = ['account.view_task']

    def get_context_data(self, *args, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.get_context_data' % (executor, self.__class__.__name__)
        context = super(ListUserTaskView, self).get_context_data(**kwargs)
        tasks = Task.objects.filter(assignation=executor)
        page_obj = self.get_paginated_list(tasks)
        context['page_obj'] = page_obj
        return context
