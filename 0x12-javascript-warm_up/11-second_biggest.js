#!/usr/bin/node
const argv = process.argv;

if (argv.length < 4) {
  console.log(0);
} else {
  const N = argv.slice(2);
  const Nsort = N.sort(function (a, b) { return Number.parseInt(a) - Number.parseInt(b); });
  console.log(Nsort[Nsort.length - 2]);
}
