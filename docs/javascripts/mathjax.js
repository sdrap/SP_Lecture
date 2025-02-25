window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages: {'[+]': ['boldsymbol']},
  },
  loader: {
    load: ['[tex]/boldsymbol'],
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
  chtml:{
    displayAlign: 'left',
  },
};

document$.subscribe(() => {
  MathJax.typesetPromise()
})
