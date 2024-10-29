<template>
  <div>
    <CitationTable />
    <AdditionalReferences />
  </div>
</template>

<script setup>
useSeoMeta({
  title: "Works Referenced In Annelyse Gelman's Vexations",
  ogTitle: "Works Referenced In Annelyse Gelman's Vexations",
  description:
    "The text is a tissue of quotations drawn from the innumerable centres of culture: A guide to Annelyse Gelman's Vexations",
  ogDescription:
    "The text is a tissue of quotations drawn from the innumerable centres of culture: A guide to Annelyse Gelman's Vexations",
  ogImage: "https://annelysegelman.com/images/vexations-web-covers.jpg",
});

defineOptions({ name: "home" });
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Baskervville:ital@0;1&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap");

@media (prefers-color-scheme: dark) {
  body {
    background-color: rgb(27, 27, 27);
    color: white;
  }
}
body,
button {
  font-family: "Work Sans", Futura, Helvetica, sans-serif;
  padding: 0;
  margin: 0;
}

body.noscroll {
  overflow: hidden;
}

table::-webkit-scrollbar {
  background-color: #000;
  width: 8px;
}

/* background of the scrollbar except button or resizer */
table::-webkit-scrollbar-track {
  background-color: #000;
}

/* scrollbar itself */
table::-webkit-scrollbar-thumb {
  background-color: #000;
  border-radius: 16px;
  border: 4px solid #fff;
}

.modal-contents::-webkit-scrollbar-thumb {
  background-color: #000;
  border-radius: 16px;
  border: 4px solid #fff;
}

/* set button(top and bottom of the scrollbar) */
table::-webkit-scrollbar-button {
  display: none;
}
</style>
