<script>
    import axios from "axios";
    let data = [];
    const loadData = async () => {
        const response = await axios.get("http://localhost:8000/autores/all");
        data = await response.data.data;
    };
    loadData();
</script>

<div class="table-container">
    {#if data.length == 0}
        <p style="font-size: 30px;margin-bottom:2rem;">
            No hay autores para mostrar
        </p>
    {/if}
    <div class="acciones">
        <p>Lista de Autores</p>
        <a href="/autores/agregar"><button class="button is-success">Agregar</button></a>
    </div>
    <table class="table">
        <thead>
            <tr>
                <th><abbr title="Position">Codigo del autor</abbr></th>
                <th>Nombre del autor</th>
                <th>Nacionalidad</th>
                <th>Operaciones</th>
            </tr>
        </thead>
        <tbody>
            {#each data as item}
                <tr>
                    <th>{item[0]}</th>
                    <td>{item[1]}</td>
                    <td>{item[2]}</td>
                    <td class="operaciones-td">
                        <a href="">
                            <button class="button is-warning"><img src="/edit.svg" alt="" width="25"></button>
                        </a>
                        <a href="">
                            <button class="button is-danger"><img src="/delete.svg" alt="" width="25"></button>
                        </a>
                    </td>
                </tr>
            {/each}
        </tbody>
    </table>
</div>

<style>
    .acciones {
        display: flex;
        align-items: center;
        column-gap: 15rem;
        margin-bottom: 1rem;
    }
    .acciones p {
        font-size: 25px;
    }
    .table-container {
        margin-top: 3rem;
        display: grid;
        place-items: center;
    }
</style>
