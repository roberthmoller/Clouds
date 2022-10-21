<script>
    import {labs, currentLab} from "$lib/labs";
</script>


<header class="bg-white dark:bg-gray-900">
    <div class="container flex flex-col px-6 py-4 mx-auto space-y-6 lg:h-[32rem] lg:py-16 lg:flex-row lg:items-center lg:justify-center ">
        <div class="flex flex-col justify-end w-full lg:flex-row lg:w-1/2">
            <div class="max-w-lg lg:mx-12 lg:order-2 flex flex-col items-end">
                <h1 class="text-3xl font-medium tracking-wide text-gray-800 dark:text-white lg:text-4xl">Clouds ☁️</h1>
                <p class="mt-4 text-gray-600 dark:text-gray-300">This is the implementation to my labs in the Clouds
                    course.</p>

                <div class="mt-6">
                    <a href="#"
                       on:click={() => alert("Clouds 👻")}
                    class="block px-3 py-2 font-semibold text-center text-white transition-colors duration-300 transform
                    bg-blue-500 rounded-md lg:inline hover:bg-blue-400">
                    What is the best course in EURECOM?
                    </a>
                </div>
            </div>
        </div>

        <div class="flex items-center justify-center w-full h-96 lg:w-1/2">
            <img class="object-cover w-full h-full max-w-2xl rounded-md"
                 src="/myself.jpeg"
                 on:click={() => alert("Ouch 🤕")}
            alt="A picture of myself">
        </div>
    </div>
</header>

<section class="bg-white dark:bg-gray-900">
    <div class="container px-6 py-10 mx-auto">
        <h1 class="text-3xl font-semibold text-center text-gray-800 capitalize lg:text-4xl dark:text-white">My Labs</h1>
        <div class="grid grid-cols-1 gap-8 mt-8 xl:mt-12 xl:gap-12 lg:grid-cols-2">
            {#each labs as lab, labNumber}
            <div class="flex items-end overflow-hidden bg-cover bg-bottom rounded-lg h-96"
                 on:click={()=> alert(lab.hasBeenCompleted ? "I don't know what to show you..": "Locked 🔒")}
                 style="background-image:url('{lab.photo}')">
            <div class="w-full px-8 py-4 overflow-hidden rounded-b-lg backdrop-blur-sm bg-white/60 dark:bg-gray-800/60">
                <h2 class="mt-4 text-2xl font-semibold text-gray-800 capitalize dark:text-white">Lab {labNumber} -
                    {lab.name}</h2>
                <p class="mt-2 text-lg tracking-wider text-blue-500 uppercase dark:text-blue-400 ">{lab.label}</p>
            </div>
        </div>
        {/each}
    </div>
    </div>
</section>