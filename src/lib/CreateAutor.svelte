<script>
    import axios from "axios";
    import { navigate } from "svelte-routing";
    let codigo;
    let nombre;
    let nacionalidad;

    const saveData = async (e) => {
        e.preventDefault();
        let response = await axios.post(
            "http://localhost:8000/autores/crear",
            {
                codigo_autor: codigo,
                nombre_autor: nombre,
                nacionalidad_autor: nacionalidad
            }
        );
        let data = await response.data;
        console.log(data.message);

        navigate("/", {replace: true})
    };
</script>

<form on:submit={(e) => saveData(e)}>
    <div class="field">
        <label class="label">Codigo del autor</label>
        <div class="control">
            <input class="input" type="text" placeholder="AUT001" required bind:value={codigo}/>
        </div>
    </div>

    <div class="field">
        <label class="label">Nombre del autor</label>
        <div class="control">
            <input
                class="input"
                type="text"
                placeholder="Ruben Dario"
                required
                bind:value={nombre}
            />
        </div>
    </div>

    <div class="field">
        <label class="label">Nacionalidad del autor</label>
        <div class="control">
            <input class="input" type="text" placeholder="Nicaragua" required bind:value={nacionalidad}/>
        </div>
    </div>

    <div class="field is-grouped">
        <div class="control">
            <input type="submit" class="button is-link" value="Guardar" />
        </div>
        <div class="control">
            <input
                type="button"
                class="button is-link is-light"
                value="Cancelar"
            />
        </div>
    </div>
</form>

<style>
    form {
        width: 50%;
        margin: 0 auto;
        margin-top: 4rem;
    }
</style>
