(function($) {
    /* "use strict" */
	
 var dzChartlist = function(){
	
	var screenWidth = $(window).width();	
	
	var radialChart = function(){
		 var options = {
          series: [70],
          chart: {
          height: 230,
          type: 'radialBar',
          toolbar: {
            show: false
          }
        },
        plotOptions: {
          radialBar: {
			hollow: {
              margin: 20,
              size: '65%',
              background: '#fff',
              image: undefined,
              imageOffsetX: 0,
              imageOffsetY: 0,
              position: 'front',
              dropShadow: {
                enabled: true,
                top: 3,
                left: 0,
                blur: 10,
                opacity: 0.1
              }
            },
            track: {
              background: '#F8F8F8',
              strokeWidth: '100%',
              margin: 0, // margin is in pixels
            },
        
            dataLabels: {
              show: true,
              value: {
				offsetY:-7,
                color: '#111',
                fontSize: '20px',
                show: true,
              }
            }
          }
        },
        fill: {
            colors: ['#ff720d'],
        },
        stroke: {
        },
        labels: [''],
        };

        var chart = new ApexCharts(document.querySelector("#radialChart"), options);
        chart.render();
	}
	var customerMap = function(){
         var options = {
          series: [{
          name: 'Income',
          data: [80, 24, 80, 90, 80, 70, 20, 85, 80, 45, 25, 65]
        }, {
          name: 'Expense',
          data: [40, 60, 20, 60, 60, 20, 60, 25, 40, 65, 15, 40]
        }, {
          name: 'Others',
          data: [20, 17, 5, 20, 20, 10, 15, 10, 15, 20, 60, 15]
        }],
          chart: {
          type: 'bar',
          height: 400,
		  toolbar:{
			show:false
		  }
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '47%',
            endingShape: 'rounded'
          },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
			show: true,
          width: 3,
          colors: ['transparent']
        },
		legend: {
			fontSize: '12px',
			 markers: {
			  width: 20,
			  height: 20
			},
			itemMargin: {
				  horizontal: 10,
				  vertical: 10
			  },
		},
        xaxis: {
          categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','nov','dec'],
		  labels: {
				style: {
					colors: '#787878',
					fontSize: '13px',
					fontFamily: 'Poppins',
					fontWeight: 400
					
				},
			}
        },
        yaxis: {
			labels: {
					style: {
						colors: '#787878',
						fontSize: '13px',
						fontFamily: 'Poppins',
						fontWeight: 400
						
					},
				}
        },
		colors:['#ff720d','#787878','#C4C4C4'],
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "$ " + val + " thousands"
            }
          }
        },
		responsive: [{
			breakpoint: 575,
			options: {
				series: [{
				  name: 'Income',
				  data: [80, 24, 80, 90, 80, 70]
				}, {
				  name: 'Expense',
				  data: [40, 60, 20, 60, 60, 20]
				}, {
				  name: 'Others',
				  data: [20, 17, 5, 20, 20, 10]
				}],
				chart: {
				  height: 250,
				},
				 plotOptions: {
				  bar: {
					columnWidth: '65%'
				  },
				},
				xaxis: {
				  categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun'],
				},
			},
		}]

        };

        var chart = new ApexCharts(document.querySelector("#customerMap"), options);
        chart.render();
		
	}
	
	var customerMap2 = function(){
         var options = {
          series: [{
          name: 'Income',
          data: [80, 24, 80, 90, 80, 70, 20, 85, 80, 45, 25, 65]
        }, {
          name: 'Expense',
          data: [40, 60, 20, 60, 60, 20, 60, 25, 40, 65, 15, 40]
        }, {
          name: 'Others',
          data: [20, 17, 5, 20, 20, 10, 15, 10, 15, 20, 60, 15]
        }],
          chart: {
          type: 'bar',
          height: 400,
		  toolbar:{
			show:false
		  }
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '47%',
            endingShape: 'rounded'
          },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
			show: true,
          width: 3,
          colors: ['transparent']
        },
		legend: {
			fontSize: '12px',
			 markers: {
			  width: 20,
			  height: 20
			},
			itemMargin: {
				  horizontal: 10,
				  vertical: 10
			  },
		},
        xaxis: {
          categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','nov','dec'],
		  labels: {
				style: {
					colors: '#787878',
					fontSize: '13px',
					fontFamily: 'Poppins',
					fontWeight: 400
					
				},
			}
        },
        yaxis: {
			labels: {
					style: {
						colors: '#787878',
						fontSize: '13px',
						fontFamily: 'Poppins',
						fontWeight: 400
						
					},
				}
        },
		colors:['#ff720d','#787878','#C4C4C4'],
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "$ " + val + " thousands"
            }
          }
        },
		responsive: [{
			breakpoint: 575,
			options: {
				series: [{
				  name: 'Income',
				  data: [80, 24, 80, 90, 80, 70]
				}, {
				  name: 'Expense',
				  data: [40, 60, 20, 60, 60, 20]
				}, {
				  name: 'Others',
				  data: [20, 17, 5, 20, 20, 10]
				}],
				chart: {
				  height: 250,
				},
				 plotOptions: {
				  bar: {
					columnWidth: '65%'
				  },
				},
				xaxis: {
				  categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun'],
				},
			},
		}]
		
        };

        var chart = new ApexCharts(document.querySelector("#customerMap2"), options);
        chart.render();
		
	}
	
	var customerMap3 = function(){
         var options = {
          series: [{
          name: 'Income',
          data: [80, 24, 80, 90, 80, 70, 20, 85, 80, 45, 25, 65]
        }, {
          name: 'Expense',
          data: [40, 60, 20, 60, 60, 20, 60, 25, 40, 65, 15, 40]
        }, {
          name: 'Others',
          data: [20, 17, 5, 20, 20, 10, 15, 10, 15, 20, 60, 15]
        }],
          chart: {
          type: 'bar',
          height: 400,
		  toolbar:{
			show:false
		  }
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '47%',
            endingShape: 'rounded'
          },
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
			show: true,
          width: 3,
          colors: ['transparent']
        },
		legend: {
			fontSize: '12px',
			 markers: {
			  width: 20,
			  height: 20
			},
			itemMargin: {
				  horizontal: 10,
				  vertical: 10
			  },
		},
        xaxis: {
          categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','nov','dec'],
		  labels: {
				style: {
					colors: '#787878',
					fontSize: '13px',
					fontFamily: 'Poppins',
					fontWeight: 400
					
				},
			}
        },
        yaxis: {
			labels: {
					style: {
						colors: '#787878',
						fontSize: '13px',
						fontFamily: 'Poppins',
						fontWeight: 400
						
					},
				}
        },
		colors:['#ff720d','#787878','#C4C4C4'],
        fill: {
          opacity: 1
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "$ " + val + " thousands"
            }
          }
        },
		
		responsive: [{
			breakpoint: 575,
			options: {
				series: [{
				  name: 'Income',
				  data: [80, 24, 80, 90, 80, 70]
				}, {
				  name: 'Expense',
				  data: [40, 60, 20, 60, 60, 20]
				}, {
				  name: 'Others',
				  data: [20, 17, 5, 20, 20, 10]
				}],
				chart: {
				  height: 250,
				},
				 plotOptions: {
				  bar: {
					columnWidth: '65%'
				  },
				},
				xaxis: {
				  categories: [ 'jan','Feb', 'Mar', 'Apr', 'May', 'Jun'],
				},
			},
		}]
		
        };

        var chart = new ApexCharts(document.querySelector("#customerMap3"), options);
        chart.render();
		
	}
	
	var widgetChart1 = function(){
		var options = {
		  series: [
			{
				name: 'Net Profit',
				data: [500, 500, 400, 400, 600, 600, 300, 300,500, 500,700,700],
				//radius: 12,	
			}, 				
		],
			chart: {
			type: 'area',
			height: 100,
			toolbar: {
				show: false,
			},
			zoom: {
				enabled: false
			},
			sparkline: {
				enabled: true
			}
			
		},
		
		colors:['#FF720D'],
		dataLabels: {
		  enabled: false,
		},
		markers: {
			shape: "circle",
		},

		legend: {
			show: false,
		},
		stroke: {
		  show: true,
		  width: 3,
		  curve:'straight',
		  colors:['#FF720D'],
		},
		
		grid: {
			show:false,
			borderColor: '#eee',
			padding: {
				top: 0,
				right: 0,
				bottom: 0,
				left: 0

			}
		},
		states: {
                normal: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                hover: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                active: {
                    allowMultipleDataPointsSelection: false,
                    filter: {
                        type: 'none',
                        value: 0
                    }
                }
            },
		xaxis: {
			categories: ['Jan', 'feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',],
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false
			},
			labels: {
				show: false,
				style: {
					fontSize: '12px',
				}
			},
			crosshairs: {
				show: false,
				position: 'front',
				stroke: {
					width: 1,
					dashArray: 3
				}
			},
			tooltip: {
				enabled: true,
				formatter: undefined,
				offsetY: 0,
				style: {
					fontSize: '12px',
				}
			}
		},
		yaxis: {
			show: false,
		},
		fill: {
		  opacity: 1,
		  colors:'#FAC7B6'
		},
		tooltip: {
			style: {
				fontSize: '12px',
			},
			y: {
				formatter: function(val) {
					return "$" + val + " thousands"
				}
			}
		}
		};

		var chartBar1 = new ApexCharts(document.querySelector("#widgetChart1"), options);
		chartBar1.render();
	 
	}
	var widgetChart2 = function(){
		var options = {
		  series: [
			{
				name: 'Net Profit',
				data: [500, 500, 300, 300, 600, 600, 400, 400,200, 200,500,500],
				//radius: 12,	
			}, 				
		],
			chart: {
			type: 'area',
			height: 100,
			toolbar: {
				show: false,
			},
			zoom: {
				enabled: false
			},
			sparkline: {
				enabled: true
			}
			
		},
		
		colors:['#FF720D'],
		dataLabels: {
		  enabled: false,
		},
		markers: {
			shape: "circle",
		},

		legend: {
			show: false,
		},
		stroke: {
		  show: true,
		  width: 3,
		  curve:'straight',
		  colors:['#FF720D'],
		},
		
		grid: {
			show:false,
			borderColor: '#eee',
			padding: {
				top: 0,
				right: 0,
				bottom: 0,
				left: 0

			}
		},
		states: {
                normal: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                hover: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                active: {
                    allowMultipleDataPointsSelection: false,
                    filter: {
                        type: 'none',
                        value: 0
                    }
                }
            },
		xaxis: {
			categories: ['Jan', 'feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',],
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false
			},
			labels: {
				show: false,
				style: {
					fontSize: '12px',
				}
			},
			crosshairs: {
				show: false,
				position: 'front',
				stroke: {
					width: 1,
					dashArray: 3
				}
			},
			tooltip: {
				enabled: true,
				formatter: undefined,
				offsetY: 0,
				style: {
					fontSize: '12px',
				}
			}
		},
		yaxis: {
			show: false,
		},
		fill: {
		  opacity: 1,
		  colors:'#FAC7B6'
		},
		tooltip: {
			style: {
				fontSize: '12px',
			},
			y: {
				formatter: function(val) {
					return "$" + val + " thousands"
				}
			}
		}
		};

		var chartBar1 = new ApexCharts(document.querySelector("#widgetChart2"), options);
		chartBar1.render();
	}
	var widgetChart3 = function(){
		var options = {
		  series: [
			{
				name: 'Net Profit',
				data: [300, 300, 400, 400, 200, 200, 400, 400,500, 500,700,700],
				//radius: 12,	
			}, 				
		],
			chart: {
			type: 'area',
			height: 100,
			toolbar: {
				show: false,
			},
			zoom: {
				enabled: false
			},
			sparkline: {
				enabled: true
			}
			
		},
		
		colors:['#FF720D'],
		dataLabels: {
		  enabled: false,
		},
		markers: {
			shape: "circle",
		},

		legend: {
			show: false,
		},
		stroke: {
		  show: true,
		  width: 3,
		  curve:'straight',
		  colors:['#FF720D'],
		},
		
		grid: {
			show:false,
			borderColor: '#eee',
			padding: {
				top: 0,
				right: 0,
				bottom: 0,
				left: 0

			}
		},
		states: {
                normal: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                hover: {
                    filter: {
                        type: 'none',
                        value: 0
                    }
                },
                active: {
                    allowMultipleDataPointsSelection: false,
                    filter: {
                        type: 'none',
                        value: 0
                    }
                }
            },
		xaxis: {
			categories: ['Jan', 'feb', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',],
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false
			},
			labels: {
				show: false,
				style: {
					fontSize: '12px',
				}
			},
			crosshairs: {
				show: false,
				position: 'front',
				stroke: {
					width: 1,
					dashArray: 3
				}
			},
			tooltip: {
				enabled: true,
				formatter: undefined,
				offsetY: 0,
				style: {
					fontSize: '12px',
				}
			}
		},
		yaxis: {
			show: false,
		},
		fill: {
		  opacity: 1,
		  colors:'#FAC7B6'
		},
		tooltip: {
			style: {
				fontSize: '12px',
			},
			y: {
				formatter: function(val) {
					return "$" + val + " thousands"
				}
			}
		}
		};

		var chartBar1 = new ApexCharts(document.querySelector("#widgetChart3"), options);
		chartBar1.render();
	}
	
	
 
	/* Function ============ */
		return {
			init:function(){
			},
			
			
			load:function(){
					radialChart();
					widgetChart1();	
					widgetChart2();
					widgetChart3();
					customerMap();
					customerMap2();
					customerMap3();
			},
			
			resize:function(){
			}
		}
	
	}();

	jQuery(document).ready(function(){
	});
		
	jQuery(window).on('load',function(){
		setTimeout(function(){
			dzChartlist.load();
		}, 1000); 
		
	});

	jQuery(window).on('resize',function(){
		
		
	});     

})(jQuery);

function getUrlParams(dParam) {
		var dPageURL = window.location.search.substring(1),
			dURLVariables = dPageURL.split('&'),
			dParameterName,
			i;

		for (i = 0; i < dURLVariables.length; i++) {
			dParameterName = dURLVariables[i].split('=');

			if (dParameterName[0] === dParam) {
				return dParameterName[1] === undefined ? true : decodeURIComponent(dParameterName[1]);
			}
		}
	}

(function($) {
	var direction =  getUrlParams('dir');
    
	if(direction == 'rtl')
	{
        direction = 'rtl'; 
    }else{
        direction = 'ltr'; 
    }

	var dezSettingsOptions = {
		typography: "poppins",
		version: "dark",
		layout: "vertical",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		//sidebarStyle: "compact",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
		
	new dezSettings(dezSettingsOptions); 

	jQuery(window).on('resize',function(){
        /*Check container layout on resize */
        dezSettingsOptions.containerLayout = $('#container_layout').val();
        /*Check container layout on resize END */
        
		new dezSettings(dezSettingsOptions); 
	});

	
	/* Dz Theme Demo Settings  */
	var dezThemeSet1 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_1",
		headerBg: "color_1",
		navheaderBg: "color_12",
		sidebarBg: "color_12",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
	
	var dezThemeSet2 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_9",
		headerBg: "color_1",
		navheaderBg: "color_9",
		sidebarBg: "color_9",
		sidebarStyle: "mini",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
	
	
	var dezThemeSet3 = {
		typography: "poppins",
		version: "dark",
		layout: "vertical",
		primary: "color_7",
		headerBg: "color_1",
		navheaderBg: "color_7",
		sidebarBg: "color_7",
		sidebarStyle: "modern",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
	
	var dezThemeSet4 = {
		typography: "poppins",
		version: "dark",
		layout: "vertical",
		primary: "color_1",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_1",
		sidebarStyle: "mini",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
	
	var dezThemeSet5 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_1",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_1",
		sidebarStyle: "mini",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
	
	var dezThemeSet6 = {
		typography: "poppins",
		version: "light",
		layout: "horizontal",
		primary: "color_5",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "static",
		containerLayout: "full",
		direction: direction
	};
	
	var dezThemeSet7 = {
		typography: "poppins",
		version: "light",
		layout: "horizontal",
		primary: "color_2",
		headerBg: "color_1",
		navheaderBg: "color_1",
		sidebarBg: "color_2",
		sidebarStyle: "compact",
		sidebarPosition: "fixed",
		headerPosition: "static",
		containerLayout: "full",
		direction: direction
	};
	
	var dezThemeSet8 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_15",
		headerBg: "color_1",
		navheaderBg: "color_15",
		sidebarBg: "color_1",
		sidebarStyle: "overlay",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "wide-boxed",
		direction: direction
	};
	
	var dezThemeSet9 = {
		typography: "poppins",
		version: "light",
		layout: "horizontal",
		primary: "color_14",
		headerBg: "color_14",
		navheaderBg: "color_14",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
	
	var dezThemeSet10 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_8",
		headerBg: "color_1",
		navheaderBg: "color_8",
		sidebarBg: "color_8",
		sidebarStyle: "compact",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
	
	var dezThemeSet11 = {
		typography: "poppins",
		version: "light",
		layout: "vertical",
		primary: "color_9",
		headerBg: "color_9",
		navheaderBg: "color_1",
		sidebarBg: "color_1",
		sidebarStyle: "full",
		sidebarPosition: "fixed",
		headerPosition: "fixed",
		containerLayout: "full",
		direction: direction
	};
	
	/* jQuery('.dz_theme_demo_1').on('click', function(){
		dzThemeDemoSet =  jQuery(this).attr('dz-theme-demo');
		new dezSettings(dzThemeDemoSet);
	}); */
	
	jQuery(document).on('click', '.dz_theme_demo', function(){
		var demoTheme = jQuery(this).data('theme');
		var ltrThemeSettings = {};
		ltrThemeSettings = eval('dezThemeSet'+demoTheme);
		ltrThemeSettings.direction = 'ltr';
		new dezSettings(ltrThemeSettings);
	});


	jQuery(document).on('click', '.dz_theme_demo_rtl', function(){
		var demoTheme = jQuery(this).data('theme');
		var rtlThemeSettings = {};
		rtlThemeSettings = eval('dezThemeSet'+demoTheme);
		
		rtlThemeSettings.direction = 'rtl';
		
		new dezSettings(rtlThemeSettings);
	});	
	
	

})(jQuery);