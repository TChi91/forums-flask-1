// topic Delete
$(function ()
 {
    $(".deleted").click(function()
    {
        var id = $(this).data('id');

        $.ajax({
            type: "DELETE",
            url: "/api/topic/delete/"+id,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response)
            {
                alert("Topic deleted successfully !");
                location.reload();
            }
        });
    });
 });



//Topic Add
$(function ()
{
    $("form").submit(function (event)
    {
        event.preventDefault();

        var topicTitle = $("input[name='title']").val();
        var topicContent = $("textarea[name='content']").val();
        var topicData = {
            "title": topicTitle,
            "content": topicContent
            };

        $.ajax({
            type: "POST",
            url: "/api/topic/add",
            data: JSON.stringify(topicData),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response)
            {
                alert("Added topic successfully !");
                window.location.href = "index"
            }
        });
    });
});
