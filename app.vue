<template>
  <div>
    <div class="page-title">
      <h1>Vexations References</h1>
    </div>
    <CitationTable />
  </div>
</template>

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

.page-title {
  height: 60px;
  width: 100%;
}

.page-title h1 {
  padding: 16px;
  font-size: 24px;
  font-weight: normal;
  margin: 0px;
}
</style>
