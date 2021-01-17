var urlPath = "https://cors-anywhere.herokuapp.com/https://traffic.dot.ga.gov/ATSPM/DefaultCharts/GetTMCMetric";
var intervalVar;
var str = "";
var headerStr="";
var needHeader = true;
var startDownloadDate="";
var signalID=0;
function GetMetricLoop()
{
	headerStr="";
	str = "";
	needHeader = true;
	if($('#signalId').val() === "")
	{
		return;
	}
	$("#btnGetData").html("downloading");
	startDownloadDate = $("#startDatepicker" ).datepicker({ dateFormat: 'dd-mm-yy' }).val();
	intervalVar = setInterval(UpdateAndSend, 5000);
	signalID = $('#signalId').val();
}

function UpdateAndSend()
{
	
	if(new Date($('#startDatepicker').val()) <= new Date($('#endDatepicker').val()))
	{
		var tosend = {
		EndDate: "",
		MetricTypeID: 5,
		SelectedBinSize: "15",
		ShowDataTable: true,
		ShowLaneVolumes: true,
		ShowTotalVolumes: true,
		SignalID: "11",
		StartDate: "",
		Y2AxisMax: "300",
		Y2AxisMin: undefined,
		YAxisMax: "1000",
		YAxisMin: undefined
		};
		var currentDate = $("#startDatepicker" ).datepicker({ dateFormat: 'dd-mm-yy' }).val();
		tosend.StartDate = $('#startDatepicker').val() + " 12:00 AM";
		tosend.EndDate = $('#startDatepicker').val() + " 11:59 PM";
		tosend.SignalID = $('#signalId').val();
		GetMetric(tosend,currentDate);
		IncrementStartDate();
	}
	else
	{
		clearInterval(intervalVar);
		var fileName = "atspm_signalID_" + signalID +"_start_download_date_"+ startDownloadDate +".csv";
		exportToCSV(headerStr+str, fileName ,'text/plain');
		$("#btnGetData").html("GetData");
	}
}

function IncrementStartDate()
{
  	var date2 = $('#startDatepicker').datepicker('getDate', '+1d'); 
  	date2.setDate(date2.getDate()+1); 
  	$('#startDatepicker').datepicker('setDate', date2);
}

function GetMetric(tosend,currentDate)
{
    $.ajax({
        url: urlPath,
        type: "POST",
        cache: false,
        async: true,
        datatype: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(tosend),
        success: function (data) {
            $('#ReportPlaceHolder').html(data);
            $('#ReportPlaceHolder').focus();
	    gatherData(tosend,currentDate);
        },
        beforeSend: function () {
        },
        complete: function () {
        },
        error: function(xhr, status, error) {
            $('#ReportPlaceHolder').html(xhr.responseText);
        }
    });
}

function gatherData(tosend,currentDate)
{
	var dataTables = document.getElementsByClassName("table table-bordered table-striped table-condensed");
	if(dataTables.length==0)
	{
		return;
	}

	var dataTable = dataTables[0] ;
	var rows = dataTable.querySelectorAll("tr");

	var canWrite = false;
	var headerCounter = 0;
	for (var i = 0; i < rows.length; i++)
	{
    		canWrite = false;
		//table header
		if(needHeader == true)
		{ 
			var headers = rows[i].querySelectorAll("th");
			headerStr +=",";
			for(var j=0; j <headers.length; j++)
			{
				headerStr +=",";
				headerStr += headers[j].firstChild.data.trim();
				
			}
			headerStr +="\n";
			headerCounter += 1;
			if(headerCounter===3)
			{
				needHeader = false;
			} 
		}

		//table data
		if(needHeader ==false && rows[i].textContent.search("Total")==-1)
		{
			var cells = rows[i].querySelectorAll("td");
			for(var j=0; j <cells.length; j++)
			{
				if(canWrite == false)
				{
					canWrite = true;
					str+=currentDate;
				}

				str +=",";
				str += cells[j].firstChild.data.trim();
			}
		}

		if(canWrite == true)
		{
			str+="\n";
		}
	}
	
}

function exportToCSV(strData, strFileName, strMimeType) 
{
    var D = document,
        A = arguments,
        a = D.createElement("a"),
        d = A[0],
        n = A[1],
        t = A[2] || "text/plain";

    //build download link:
    a.href = "data:" + strMimeType + "charset=utf-8," + escape(strData);


    if (window.MSBlobBuilder) 
{ // IE10
        var bb = new MSBlobBuilder();
        bb.append(strData);
        return navigator.msSaveBlob(bb, strFileName);
    } /* end if(window.MSBlobBuilder) */



    if ('download' in a) 
	{ //FF20, CH19
        a.setAttribute("download", n);
        a.innerHTML = "downloading...";
        D.body.appendChild(a);
        setTimeout(function() {
            var e = D.createEvent("MouseEvents");
            e.initMouseEvent("click", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            a.dispatchEvent(e);
            D.body.removeChild(a);
        }, 66);
        return true;
    }; /* end if('download' in a) */



    //do iframe dataURL download: (older W3)
    var f = D.createElement("iframe");
    D.body.appendChild(f);
    f.src = "data:" + (A[2] ? A[2] : "application/octet-stream") + (window.btoa ? ";base64" : "") + "," + (window.btoa ? window.btoa : escape)(strData);
    setTimeout(function() 
    {
        D.body.removeChild(f);
    }, 333);
    return true;
}