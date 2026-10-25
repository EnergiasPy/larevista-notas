<?php
// xlsx-lib.php · lector mínimo de .xlsx (sin dependencias) para fuentes oficiales de combustibles
function xlsx_sheets($file) {
  $z = new ZipArchive();
  if ($z->open($file) !== true) return null;
  $ss = [];
  if (($x = $z->getFromName('xl/sharedStrings.xml')) !== false) {
    $sx = simplexml_load_string($x);
    foreach ($sx->si as $si) {
      if (isset($si->t)) $ss[] = (string)$si->t;
      else { $t = ''; foreach ($si->r as $r) $t .= (string)$r->t; $ss[] = $t; }
    }
  }
  $wb = simplexml_load_string($z->getFromName('xl/workbook.xml'));
  $rels = simplexml_load_string($z->getFromName('xl/_rels/workbook.xml.rels'));
  $map = []; foreach ($rels->Relationship as $r) $map[(string)$r['Id']] = (string)$r['Target'];
  $out = [];
  foreach ($wb->sheets->sheet as $s) {
    $rid = (string)$s->attributes('http://schemas.openxmlformats.org/officeDocument/2006/relationships')['id'];
    $t = $map[$rid] ?? ''; $t = ltrim(preg_replace('#^/?xl/#', '', $t), '/');
    $out[(string)$s['name']] = 'xl/' . $t;
  }
  return [$z, $ss, $out];
}
function xlsx_rows($z, $ss, $path, $max = 0) {
  $x = $z->getFromName($path); if ($x === false) return [];
  $sx = simplexml_load_string($x); $rows = [];
  foreach ($sx->sheetData->row as $row) {
    $r = [];
    foreach ($row->c as $c) {
      $ref = (string)$c['r']; $col = 0;
      for ($i = 0; $i < strlen($ref) && ctype_alpha($ref[$i]); $i++) $col = $col * 26 + (ord($ref[$i]) - 64);
      $v = isset($c->v) ? (string)$c->v : (isset($c->is->t) ? (string)$c->is->t : '');
      if ((string)$c['t'] === 's') $v = $ss[(int)$v] ?? '';
      $r[$col - 1] = $v;
    }
    if ($r) { $m = max(array_keys($r)); $f = []; for ($i = 0; $i <= $m; $i++) $f[] = $r[$i] ?? ''; $rows[] = $f; }
    if ($max && count($rows) >= $max) break;
  }
  return $rows;
}
