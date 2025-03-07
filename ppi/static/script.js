$(document).ready(function() {
    $('#deleteButton').click(function() {
        var projetoId = $(this).data('id');
        $('#deleteForm').attr('action', '/projeto/excluir/' + projetoId + '/');
        $('#deleteModal').modal('show');
    });
});
function projetosPaginacao() {
    $(".link-pag").click(function(evento) {
        evento.preventDefault();
        const url = $(this).data("url");
        $.get(url, function(resposta) {
            $("#lista-projetos").html(resposta);
            projetosPaginacao();
        });
    });
}
projetosPaginacao();
