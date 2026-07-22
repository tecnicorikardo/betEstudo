import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { __test } from "../src/worker.js";

const readMarkdown = (filename) => readFileSync(new URL(`../${filename}`, import.meta.url), "utf8");

const tiLessons = __test.parseTiSchedule(readMarkdown("cronograma_ti_20_semanas_detalhado.md"));
assert.equal(tiLessons.length, 100);
assert.equal(__test.lessonForBusinessDate(tiLessons, "2026-06-01", "2026-06-01")?.weekdayName, "Segunda-feira");
assert.equal(__test.lessonForBusinessDate(tiLessons, "2026-06-01", "2026-06-06"), null);

const englishLessons = __test.parseWeekdaySchedule(readMarkdown("Guia Completo_ Frases do Cotidiano Americano.md"));
assert.equal(englishLessons.size, 5);
assert.match(englishLessons.get(0)?.title || "", /Saudações/);

const grammarLessons = __test.parseWeekdaySchedule(readMarkdown("gramatica.md"));
assert.equal(grammarLessons.size, 5);
assert.match(grammarLessons.get(0)?.title || "", /TO BE/);

const bibleLessons = __test.parseBibleSchedule(readMarkdown("resumo_novo_testamento.md"));
assert.equal(bibleLessons.length, 260);
assert.equal(__test.sequentialLessonForDate(bibleLessons, "2026-06-01", "2026-06-01")?.title, "Evangelho de Mateus 1");

console.log("Worker parsers OK");
