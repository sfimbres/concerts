<template>
    <h1>Home Page</h1>

    <ul>
        <li><NuxtLink to="/concerts/1">Concert 1</NuxtLink></li>
        <li><NuxtLink to="/concerts/2">Concert 2</NuxtLink></li>
    </ul>

    <Card />
    <Card />
    <Card />
    <Card />
    <Card />
    <Card />
    <Card />
    <Card />
    <Card />

</template>

<script setup>
    import Card from '~/components/Card.vue';
</script>