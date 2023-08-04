<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
    $('#id_type_nomenclature_sp_fk').change(function() {
        var typeId = $(this).val();
        $.ajax({
            type: 'GET',
            url: '/get_materials/',  // Замените на вашу URL-адрес
            data: {'type_id': typeId},
            success: function(data) {
                $('#id_material_fk').html(data);
            }
        });
    });
});
</script>
