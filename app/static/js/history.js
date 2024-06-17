$(document).ready(function() {
    var table = $('#history-table').DataTable({
        "paging": true,
        "searching": true,
        "ordering": true,
        "info": true,
        "lengthChange": true,
        "pageLength": 10,
        "scrollx":true,
        "language": {
            "search": "Filter records:",
            "lengthMenu": "Show _MENU_ entries",
            "info": "Showing _START_ to _END_ of _TOTAL_ entries",
            "infoEmpty": "No entries available",
            "infoFiltered": "(filtered from _MAX_ total entries)"
        }
    });
    $('#instrument-type-search').on('change', function() {
        var searchValue = $(this).val();
        table.column(1).search(searchValue).draw();
    });

});



