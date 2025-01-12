
const pesquisarBtn = document.getElementById('pesquisar');

if (pesquisarBtn) {
    pesquisarBtn.addEventListener('click', () => {
        event.stopPropagation();
        pesquisarBtn.classList.toggle('mudarTamanho')
    });
    
    document.addEventListener('click', function() {
        pesquisarBtn.classList.remove('mudarTamanho');
    });
}