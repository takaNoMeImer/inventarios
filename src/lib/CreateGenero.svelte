<script>
    import axios from "axios";
    import { navigate } from "svelte-routing";
    let codigo;
    let nombre;
    let descripcion;

    const saveData = async (e) => {
        e.preventDefault();
        let response = await axios.post(
            "http://localhost:8000/generos/crear",
            {
                nombre_genero: nombre,
                descripcion: descripcion
            }
        );
        let data = await response.data;
        console.log(data.message);

        navigate("/", {replace: true})
    };
</script>

<form on:submit={(e) => saveData(e)}>
    <!-- <div class="field hidden">
        <label class="label">Id genero</label>
        <div class="control">
            <input class="input" type="text" placeholder="AUT001" required bind:value={codigo}/>
        </div>
    </div> -->

    <div class="field">
        <label class="label">Nombre genero</label>
        <div class="control">
            <input
                class="input"
                type="text"
                placeholder="Romance"
                required
                bind:value={nombre
                }
            />
        </div>
    </div>

    <div class="field">
        <label class="label">Descripcion</label>
        <div class="control">
            <input class="input" type="text" placeholder="Romance" required bind:value={descripcion}/>
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
