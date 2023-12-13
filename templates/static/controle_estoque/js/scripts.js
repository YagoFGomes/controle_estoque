window.onload = (e) => {
  const nome_produto = document.getElementById("id_nome_produto");
  const codigo_produto = document.getElementById("id_codigo_produto");
  const quantidade = document.getElementById("id_quantidade");
  const quantidade_minima = document.getElementById("id_quantidade_minima");
  const categoria = document.getElementById("id_categoria");
  const preco_produto = document.getElementById("id_preco_custo");
  const preco_venda = document.getElementById("id_preco_venda");

  nome_produto.setAttribute("disabled", true);
  codigo_produto.setAttribute("disabled", true);
  quantidade.setAttribute("disabled", true);
  quantidade_minima.setAttribute("disabled", true);
  categoria.setAttribute("disabled", true);
  preco_produto.setAttribute("disabled", true);
  preco_venda.setAttribute("disabled", true);
};
