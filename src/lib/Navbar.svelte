<script></script>

<!-- svelte-ignore a11y-no-redundant-roles -->
<!-- svelte-ignore a11y-missing-attribute -->

<nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <a class="navbar-item" href="https://bulma.io">
            <p>INVENTARIO</p>
        </a>

        <a
            role="button"
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbarBasicExample"
        >
            <span aria-hidden="true" />
            <span aria-hidden="true" />
            <span aria-hidden="true" />
        </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
            <a href="/" class="navbar-item"> Inicio </a>

            <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link"> Autores </a>

                <div class="navbar-dropdown">
                    <a class="navbar-item"> Autor 1 </a>
                    <a class="navbar-item"> Autor 2 </a>
                    <a class="navbar-item"> Autor 3 </a>
                </div>
            </div>

            <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link"> Generos </a>

                <div class="navbar-dropdown">
                    <a class="navbar-item"> Genero 1 </a>
                    <a class="navbar-item"> Genero 2 </a>
                    <a class="navbar-item"> Genero 3 </a>
                </div>
            </div>

            <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link"> Libros </a>

                <div class="navbar-dropdown">
                    <a class="navbar-item"> Libro 1 </a>
                    <a class="navbar-item"> Libro 2 </a>
                    <a class="navbar-item"> Libro 3 </a>
                </div>
            </div>

            <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link"> Editoriales </a>

                <div class="navbar-dropdown">
                    <a class="navbar-item"> Editorial 1 </a>
                    <a class="navbar-item"> Editorial 2 </a>
                    <a class="navbar-item"> Editorial 3 </a>
                </div>
            </div>
        </div>

        <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                    <a class="button is-primary">
                        <strong>Sign up</strong>
                    </a>
                    <a class="button is-light"> Log in </a>
                </div>
            </div>
        </div>
    </div>
</nav>

<style></style>
