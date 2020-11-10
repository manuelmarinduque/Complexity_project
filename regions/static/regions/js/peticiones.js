function SaveData(csrf_token) {
    form = document.querySelector('#region_form');
    let data_form = new FormData(form);
    fetch('/region_create/', {
        method: "POST",
        body: data_form,
        headers: {
            "X-CSRFToken": csrf_token,
        }
    }).then(
        function (response) {
            return response.json();
        }
    ).then(
        function (data) {
            ShowMessage(data.message);
            GetData();
        }
    ).catch(
        function (response) {
            console.log(response);
        }
    )
}

function GetData() {
    fetch('/region_list/'
    ).then(
        function (response) {
            return response.json();
        }
    ).then(
        function (data) {
            console.log(data);
            showData(data);
        }
    ).catch(
        function (response) {

        }
    )
}

function ShowMessage(message) {
    my_div = document.querySelector('#success_message');
    removeChilds(my_div);
    my_div.classList.add('alert', 'alert-success');
    const div = document.createElement('div');
    div.innerHTML = `
        <p> ${message} </p>
    `;
    my_div.appendChild(div);
}

function showData(data) {
    table_body = document.querySelector('#data_table tbody');
    removeChilds(table_body);
    for (const region of data) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td> ${region.fields.region_name} </td>
            <td> ${region.fields.existing_population} </td>
            <td> ${region.fields.current_personal} </td>
            <td> ${region.fields.required_personal} </td>
            <td> ${region.fields.generated_costs} </td>
            <td> ${region.fields.deads} </td>
            <td> ${region.fields.qualification} </td>
        `;
        table_body.appendChild(row);
    }
}

function removeChilds(element) {
    while (element.firstElementChild) {
        element.removeChild(element.firstElementChild);
    }
}