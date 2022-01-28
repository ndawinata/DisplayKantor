$(document).ready(function () {

    var tabledata = [
        {id:1, pnbp:"Informasi Cuaca untuk Pelayaran", satuan:"per route \nper hari", tarif:"Rp. 250.000,00"},
        {id:2, pnbp:"Informasi Cuaca untuk Pelabuhan", satuan:"per route \nper hari", tarif:"Rp. 225.000,00"},
        {id:3, pnbp:"Informasi Cuaca untuk Pengeboran Lepas", satuan:"per route \nper hari", tarif:"Rp. 330.000,00"},
    ];

    navigator.getUserMedia({ video: true}, function (stream) {
        if (stream.getVideoTracks().length > 0 ) {
            //code for when none of the devices are available                       
        } else {
           // code for when both devices are available
        }
    }, function (error) { 
      // code for when there is an error
    });

    var table = new Tabulator("#example-table", {
        data:tabledata, //assign data to table,
        height:500,
        layout:"fitColumns", //fit columns to width of table (optional)
        columns:[ //Define Table Columns
            {title:"Jenis Penerimaan Negara Bukan Pajak", field:"pnbp", width:300},
            {title:"Satuan", field:"satuan", width:150},
            {title:"Tarif", field:"tarif", width:150},
        ],
    });
    
    //trigger an alert message when the row is clicked
    table.on("rowClick", function(e, row){ 
        alert("Row " + row.getData().id + " Clicked!!!!");
    });
});
