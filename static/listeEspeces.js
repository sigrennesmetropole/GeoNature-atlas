
/*// sort the table
$(document).ready(function() 
    { 
        $("#myTable")
        .tablesorter();

    } 
); 
*/


$(document).ready(function(){
    $('#myTable').DataTable({
    	"order":[3, 'desc'],
    	"lengthChange": false,
    	"pageLength": 50,
        "oLanguage": {
           "sSearch": "",
            "sInfo": "",
            "sInfoEmpty": "",
            "sInfoFiltered": "",
            "sZeroRecords": "Aucune espèce trouvée",

        "oPaginate": {
           "sPrevious": "Précedent",
           "sNext" : "Suivant"
         }
      },
    });
    $('.dataTables_filter input').attr("placeholder", "Rechercher dans la liste ").attr("class", "form-control").css("font-weight", "normal");
    $('.dataTables_empty').text("rien")

});


// change de glyphicon

$('th').click( function(){
    $(this).find('span').toggleClass('glyphicon glyphicon-menu-down').toggleClass('glyphicon glyphicon-menu-up');
});

    