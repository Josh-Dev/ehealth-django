$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip();
});
$(document).ready(function(){
    $('[data-toggle="popover"]').popover({trigger: "hover"});
});

var $gp;

function setSelectedPage(thePage) {
    var par = $(thePage).parent()[0];
    $gp = $(par).parent();
    $('#hfPage').val(gp);
}

function savePage() {
    //get api uri
    var uri = 'save_page'

    //get data
    var fol_name = $('#fol_name').val()
    var summary = $gp.children('#resSummary').text();
    var url = $gp.find('#resLink').attr('href');
    var title = $gp.find('#resLink').text();


    alert('gp  :' + $gp + ' || url : ' + url + ' || folder name : ' + fol_name + ' || title : ' + title + ' || summary : ' + summary)

    var data = { 'folder_name': fol_name, 'url': url, 'title': title, 'desc': summary }
    $.get(uri, data, function(returned) {
        //If successful close modal
        $('#modalSave').modal('hide');
        alert(returned)
    })
}

function deleteFolder(folder_id) {
    var uri = "../../delete_folder"

    if (confirm("Are you sure you want to delete the folder? All the pages will be deleted too!")) {
        //
        $.get(uri, {'folder_id':folder_id}, function(returned) {
            location.reload(true);
        })
    }

}

function deletePage(page_name) {
    var uri = "delete_page"

    if (confirm("Are you sure you want to delete the page?")) {

    }
}
