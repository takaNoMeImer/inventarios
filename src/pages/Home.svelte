<script>
    import Element from "../lib/Element.svelte";
</script>
<div class="elements">
    <Element messageButton={"Ver libros"} title_card={"Libros"} link={"libros"} image={"https://images.vexels.com/media/users/3/139752/isolated/preview/532e26143a0435e9c6ca7f436474389f-icono-de-libros.png"}/>
    <Element messageButton={"Ver autores"} title_card={"Autores"} link={"autores"} image={"https://www.editorialrenacimiento.com/themes/renacimiento2016/images/no-autor.png"}/>
    <Element messageButton={"Ver editoriales"} title_card={"Editoriales"} link={"editoriales"} image={"https://seeklogo.com/images/E/editorial-planeta-logo-12835CA6FA-seeklogo.com.png"}/>
    <Element messageButton={"Ver generos"} title_card={"Generos"} link={"generos"} image={"https://www.shutterstock.com/image-vector/tragedy-literary-genre-book-icon-260nw-1830363194.jpg"}/>
</div>
<style>
    .elements {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1rem;
        margin-top: 4rem;
    }
</style>