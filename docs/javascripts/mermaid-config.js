document$.subscribe(() => {
  mermaid.initialize({
    startOnLoad: true,
    securityLevel: "loose", // Needed for inline HTML in Mermaid
    theme: "dark",             // Use the default theme
    layout: "elk",               // Use ELK for all diagrams
    elk: {
      nodePlacementStrategy: "LINEAR_SEGMENTS",
      mergeEdges: false,
      // Add other ELK settings if desired, e.g.:
      // mergeEdges: true,
      // randomSeed: 1,
      // etc.
    }
  });

  mermaid.init(undefined, document.querySelectorAll(".mermaid"));
});

