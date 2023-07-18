$(document).ready(function(){
    $("#userInput").on("submit", function(e){
        e.preventDefault();
        var userText = $("#textInput").val();
        $("#textInput").val("");
        var temp = "<p class='userMessage'>"+userText+"</p>";
        $("#chatbox").append(temp);
        $.ajax({
            url: "/get",
            method: "POST",
            data: {msg: userText},
            success: function(result){
                var botHtml = "<p class='botMessage'>"+result.msg+"</p>";
                $("#chatbox").append(botHtml);
            }
        });
    });
});
