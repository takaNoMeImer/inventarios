<script>
    export let messageButton;
    export let title_card;
    export let link;
    export let image;
</script>

<div
    class="flex justify-between py-8 px-8 w-5/6 mx-auto bg-white rounded-xl shadow-lg space-y-2 sm:py-4 sm:flex sm:items-center sm:space-y-0 sm:space-x-6"
>
    <img
        class="block  h-24 rounded-full sm:mx-0 sm:shrink-0 justify-self-start"
        src={image}
        alt="Woman's Face"
    />
    <div class="text-center space-y-2 sm:text-left">
        <div class="space-y-0.5">
            <p class="text-lg text-black font-semibold">{title_card}</p>
        </div>
        <a href={`/${link}`}>
            <button
            class="px-4 py-1 text-sm text-purple-600 font-semibold rounded-full border border-purple-200 hover:text-white hover:bg-purple-600 hover:border-transparent focus:outline-none focus:ring-2 focus:ring-purple-600 focus:ring-offset-2"
            >{messageButton}</button
        >
        </a>
    </div>
</div>

<style></style>
