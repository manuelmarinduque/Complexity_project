function SaveData(csrf_token) {
    form = document.getElementById('region_form');
    var data_form = new FormData(form);
    fetch('/region_create/', {
        method: "POST",
        body: data_form,
        headers: {
            "X-CSRFToken": csrf_token,
        }
    }).then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {
            console.log(data);
            ShowMessage(data.message);
        }
    ).catch(
        function (response) {
            console.log(response.json());
        }
    )
}

function GetData() {
    fetch('/region_create/', {
        method = "GET"
    }).then(
        function (response) {
            return response.json()
        }
    ).then(
        function (data) {

        }
    ).catch(
        function (response) {
            console.log(response.json());
        }
    )
}

function ShowMessage(message) {
    my_div = document.getElementById('success_message');
    var paragraph = document.createElement("p");
    paragraph.textContent = message;
    my_div.appendChild(paragraph);
}