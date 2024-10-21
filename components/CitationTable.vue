<template>
  <div class="table-wrapper" @keyup.esc="closeModal" id="top">
    <table class="full-table">
      <thead>
        <tr class="page-title">
          <th colspan="7">
            <div class="h1">
              The text is a tissue of quotations drawn from the innumerable
              centres of culture<sup>1</sup>:
            </div>
            <div class="h2">
              A guide to the references in Annelyse Gelman's <i>Vexations</i>
            </div>
            <a
              class="attribution"
              href="https://annelysegelman.com/pdf/barthes-deathoftheauthor.pdf"
              target="_blank"
              rel="noopener noreferrer"
            >
              1. Roland Barthes, <i>The Death of the Author </i>
              <ExternalLink purple />
            </a>

            <nuxt-link class="jump" :to="anchorDestination" external>
              Jump to additional references below
            </nuxt-link>
          </th>
        </tr>

        <tr>
          <th class="headers"></th>
          <th
            v-for="col in headers"
            :key="col"
            class="headers"
            v-html="col"
          ></th>
        </tr>
        <tr>
          <th class="header-divider" colspan="7"></th>
        </tr>
      </thead>
      <tbody class="text">
        <tr
          v-for="row in citations"
          :key="row.id"
          @click="openModal(row)"
          class="row"
          :class="hasContent(row) ? 'clickable' : 'not-clickable'"
        >
          <td class="table-cell">
            <span v-if="hasContent(row)"
              ><PaperclipIcon class="paperclip"
            /></span>
          </td>
          <td v-for="col in headers" :key="col" class="table-cell cols">
            <span v-if="col === 'Referenced'">
              <a
                v-if="row.Link && row[col]"
                :href="row.Link"
                target="_blank"
                rel="noopener noreferrer"
                @click.stop
              >
                {{ row[col] }}
                <ExternalLink />
              </a>
              <span v-else-if="!row.Link">
                {{ row[col] }}
              </span>
              <a v-else :href="row.Link" target="_blank" @click.stop>
                <span class="see-more">(See more)</span> <ExternalLink
              /></a>
            </span>
            <span
              v-else-if="col.includes('Line')"
              v-html="row[col]"
              class="full-line"
            ></span>
            <span v-else>{{ row[col] }}</span>
          </td>
        </tr>
      </tbody>
    </table>
    <div
      v-if="modal"
      class="hover-el"
      @click="closeModal"
      ref="modalref"
      tabindex="0"
    >
      <DetailModal
        :author="author"
        :source="source"
        :modal-content="modalContent"
        :picture="picture"
        @close="closeModal"
      />
    </div>
  </div>
</template>

<script setup>
import citations from "~/public/citations.js";
import ExternalLink from "./ExternalLink.vue";
import PaperclipIcon from "./PaperclipIcon.vue";
import DetailModal from "./DetailModal.vue";

const picture = ref("");
const modalContent = ref("");
const author = ref("");
const source = ref("");
const modalref = ref(null);
const modal = ref(false);
const openModal = (row) => {
  if (hasContent(row)) {
    modal.value = true;
    picture.value = row["File"];
    modalContent.value = row["Hover element"];
    author.value = row["Author"];
    source.value = row["Referenced"];
    nextTick(() => {
      modalref.value.focus();
    });
  }
  document.body.classList.add("noscroll");
};

const closeModal = () => {
  modal.value = false;
  picture.value = "";
  author.value = "";
  source.value = "";
  document.body.classList.remove("noscroll");
};

const hasContent = (row) => {
  return !!row["File"] || !!row["Hover element"];
};

const headers = Object.keys(citations[0]).filter(
  (item) =>
    item !== "id" &&
    item !== "Hover element" &&
    item !== "File" &&
    item !== "Link" &&
    item !== ""
);

const anchorDestination = import.meta.env.PROD
  ? {
      path: "https://annelysegelman.com/vexations-references/",
      hash: "#additional",
    }
  : { name: "home", hash: "#additional" };
</script>

<style scoped>
.page-title {
  height: 210px;
  width: 100%;
}

.page-title .h1 {
  padding: 16px 16px 16px 50px;
  font-size: 20px;
  font-weight: normal;
  margin: 0px;
  width: calc(100vw - 100px);
  position: sticky;
  color: #823061;
  left: 2px;
}

.page-title .h2 {
  padding-left: 50px;
  font-size: 24px;
  font-weight: normal;
  margin-bottom: 20px;
  width: calc(100vw - 100px);
  position: sticky;
  left: 2px;
}

.page-title .attribution {
  padding-left: 50px;
  font-weight: normal;
  width: calc(100vw - 100px);
  position: sticky;
  left: 2px;
  color: #823061;
  text-decoration-color: transparent;
  transition: text-decoration-color 150ms ease;
  display: block;
}
.page-title .attribution:hover {
  text-decoration-color: #823061;
}
.jump {
  margin-top: 6px;
  padding-left: 50px;
  font-weight: normal;
  width: calc(100vw - 100px);
  position: sticky;
  left: 2px;
  display: block;
  font-style: italic;
}

a {
  text-decoration-color: transparent;
  transition: text-decoration-color 150ms ease;
  color: #0071c5;
}
a:hover {
  text-decoration-color: #0071c5;
}
.see-more {
  font-style: italic;
}

.full-table {
  text-align: left;
  position: relative;
  padding: 0px;
  border-collapse: collapse;
}

.table-cell {
  padding: 14px 0px;
  border: none;
  border-spacing: 0;
  overflow: hidden;
}

.headers {
  background: white;
  position: sticky;
  top: 0px;
  padding-top: 10px;
  padding-bottom: 10px;
  border: none;
  border-spacing: 0;
  height: 44px;
}

.table-wrapper {
  max-height: 100dvh;
  overflow: auto;
}

.full-line {
  min-width: 250px;
}

.cols {
  padding-right: 10px;
  padding-left: 12px;
}

.hover-el {
  position: absolute;
  top: 0;
  height: 100dvh;
  width: 100vw;
  background-color: #00000088;
  display: flex;
  align-items: center;
  justify-content: center;
}
.row {
  border-bottom: 1px solid rgba(0, 0, 0, 0.17);
}
.row:hover {
  transition: background-color ease-in-out 150ms;
  background-color: #ffffb7;
}
.clickable {
  cursor: pointer;
}
.not-clickable {
  cursor: default;
}

.header-divider {
  background-color: black;
  height: 1px;
  padding: 0;
  margin: 0;
  position: sticky;
  top: 64px;
}

.headers {
  padding: 10px;
}

.paperclip {
  padding-left: 10px;
  padding-right: 10px;
}

.back-top {
  position: absolute;
}

@media (prefers-color-scheme: dark) {
  .headers {
    background: rgb(27, 27, 27);
  }
  .row:hover {
    background-color: #303022;
  }
  .row {
    border-bottom: 1px solid rgba(255, 255, 255, 0.17);
  }
  .header-divider {
    background-color: rgb(190, 190, 190);
  }
  .page-title .h1 {
    color: #d793bc;
  }
  .page-title .attribution {
    color: #d793bc;
  }
  .page-title .attribution:hover {
    text-decoration-color: #d793bc;
  }
}
</style>
