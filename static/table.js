function selectRow(id) {
    var active = document.getElementsByClassName("table-active");
    if(active.element)
        for (let element in active)
            element.classList.remove("table-active");

    var row = document.getElementById("row" + id);
    row.classList.add("table-active");
}