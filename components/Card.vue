<template>
    <NuxtLink :to="{ path: `/concerts/${slugify(concert.headliner)}-${formatDate(concert.date_from)}`, query: {cid:cid} }">
        <div class="container mx-auto my-4 px-4 aspect-video bg-blue-100 flex flex-col-reverse">
            <div class="w-9/12 my-4">
                <h2 class="text-xl font-bold">{{ concert.headliner }}</h2>
                <h3 class="text-sm">{{ concert.artists.join(', ') }}</h3>
                <p class="text-xs">{{ concert.date_from }} • {{ concert.venue }} • {{ concert.location }}</p>
            </div>
        </div>
    </NuxtLink>
</template>

<script setup>
defineProps({
    concert: {
        type: Object,
        required: true
    },
    cid: {
        type: Number,
        required: true
    }
});

const slugify = (str) => {
    return str.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]/g, '');
};

const formatDate = (dateStr) => {
    // Convert "November 8, 2024" to "11-08-2024"
    const date = new Date(dateStr);
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const year = date.getFullYear();
    return `${month}-${day}-${year}`;
};
</script>