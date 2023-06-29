<script>
    import Navbar from "./lib/Navbar.svelte";
    import {Router, Route} from 'svelte-routing';
    import Home from "./pages/Home.svelte";
    import Autores from "./pages/Autores.svelte";
    import Editoriales from "./pages/Editoriales.svelte";
    import Generos from "./pages/Generos.svelte";
    import CreateAutor from "./lib/CreateAutor.svelte";
    import CreateGenero from "./lib/CreateGenero.svelte";
    import CreateEditorial from "./lib/CreateEditorial.svelte";
    import Libros from "./pages/Libros.svelte";
</script>
<main>
    <Navbar />

    <Router>
        <Route path="/"> <Home /> </Route>
        <Route path="/autores"> <Autores /> </Route>
        <Route path="/autores/agregar"> <CreateAutor /> </Route>
        <Route path="/editoriales/agregar"> <CreateEditorial /> </Route>
        <Route path="/generos/agregar"> <CreateGenero /> </Route>
        <Route path="/editoriales"> <Editoriales /> </Route>
        <Route path="/generos"> <Generos /> </Route>
        <Route path="/libros"> <Libros /> </Route>
        <Route path="/libros/agregar"> <Libros /> </Route>
    </Router>
</main>
<style>
</style>