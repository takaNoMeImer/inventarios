<script>
    import axios from 'axios';
    import { navigate } from 'svelte-routing';
    let codigo;
    let nombre;
    let contacto;
    let telefono;

    let stateEditorial = "hidden"
    let stateEditorialMessage = ""
    let stateEditorialStyle = ""

    const saveData = async (e) => {
        e.preventDefault()
        let response = await axios.post("http://localhost:8000/editoriales/crear", {codigo_editorial: codigo, nombre_editorial: nombre, contacto: contacto, telefono: telefono})
        let data = await response.data
        console.log(data.message);

        // navigate("/", {replace: true})
        
        if (data.message == "La editorial ya existe") {
            stateEditorial = ""
            stateEditorialMessage = data.message
            stateEditorialStyle = "font-size: 25px; color: red;text-align:center;margin-bottom:2rem;"
            setTimeout( () => {
               stateEditorial = "hidden"
            }, 2000)
            
        } else {
            stateEditorial = ""
            stateEditorialStyle = "font-size: 25px; color: green;text-align:center;margin-bottom:2rem;"

            setTimeout(() => {
                stateEditorial = "hidden"
                navigate("/", {replace: true})
            }, 2000)
        }

    }
</script>

<!-- svelte-ignore a11y-label-has-associated-control -->
<p class={stateEditorial} style="font-size: 25px; color: red;text-align:center;margin-bottom:2rem;">{stateEditorialMessage}</p>
<form on:submit={ (e) => saveData(e)}>
    <div class="field">
        <label class="label">Codigo editorial</label>
        <div class="control">
            <input class="input" type="text" placeholder="1" required bind:value={codigo}/>
        </div>
    </div>

    <div class="field">
        <label class="label">Nombre editorial</label>
        <div class="control">
            <input class="input" type="text" placeholder="Monumental" required bind:value={nombre}/>
        </div>
    </div>

    <div class="field">
        <label class="label">Contacto</label>
        <div class="control">
            <input class="input" type="text" placeholder="Imer" required bind:value={contacto}/>
        </div>
    </div>

    <div class="field">
        <label class="label">Telefono</label>
        <div class="control">
            <input class="input" type="text" placeholder="123456789" required bind:value={telefono}/>
        </div>
    </div>
    
    <div class="field is-grouped">
        <div class="control">
            <input type="submit" class={`button is-link`} value="Guardar">
        </div>
        <div class="control">
            <input type="button" class={`button is-link is-light`} value="Cancelar">
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