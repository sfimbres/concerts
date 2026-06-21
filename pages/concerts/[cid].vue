<template>
    <div class="container mx-auto px-4">
        <h1 class="text-3xl font-bold my-8">Concerts Name</h1>
        <p>Custom ID (cid): {{ concert.cid }}</p>
        <pre>{{ concert }}</pre>
    </div>
</template>

<script setup>
//import Card from '~/components/Card.vue';
const route = useRoute();
//const cid = computed(() => String(route.query.cid ?? ''));
console.log('route parms:', route.params);
console.log('route query:', route.query);
//console.log('route cid:', cid);

const { data: concert, error } = await useAsyncData(
  () => `concert-${String(route.params.cid ?? '')}`,
  async () => {
    const cid = String(route.params.cid.split('-')[0] ?? '');
    console.log('Extracted cid:', cid);
    if (!cid) return null;
    const data = await queryCollection('concerts').where('cid', '=', cid).first();
    return data ?? null;
  }
);

console.log('Concert:', concert.value);
console.log('Concert id :', concert.value.cid);
</script>