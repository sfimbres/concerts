<template>
    <div class="container mx-auto px-4">
        <h1 class="text-3xl font-bold my-8">Concerts</h1>

        <div v-if="concerts && concerts.length" class="grid gap-4">
            <Card 
                v-for="(concert, index) in concerts" 
                :key="concert.headliner + concert.date_from"
                :concert="concert"
                :cid="index + 1"
            />
        </div>
        <div v-else>
            <p>No concerts found.</p>
        </div>
    </div>
</template>

<script setup>
import Card from '~/components/Card.vue';

const { data: concerts } = await useAsyncData('concerts', async () => {
    const data = await queryCollection('concerts').all();
    return data;
});

console.log('Concerts:', concerts.value);
</script>