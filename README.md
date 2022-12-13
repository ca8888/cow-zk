# Privacy Preserving CoW Swap Trader Leaderboard - Based on Sismo Badges

## status:
**local version with "real" users data has being made. marketing related design and text needed.**
once marketing provide the neccesry information the nadges would go online

## what is missing for going online
I am currently missing the below marketing metadata to be able to move forward

### Main url
```js
  {
    path: "cow-top-hundred", // choose your frontend path
    title: "COW", // choose your title  see in the below image next to the
    subtitle: "Show that you are top 100 cow trader.",
    logoUrl: "https://cow.fi/images/og-meta-cowprotocol.png",
    onboardingDescription: "Mint this badge to show that you are top 100 cow trader",
    ctaLabel: "Go to cow platform",
    ctaUrl: "https://cow.fi/", // provide a link to your users. If you does not have a link you can add "" this will redirect to the sismo explorer.
    congratulationTexts: ["Congratulations mooooo"],
  },
```

![badge main](local.png)

### Badge url
If the user want more details, one can press on the badge and the bellow image would appear. Here one can find the data need to change

```js
    {
      name: "cow top 100", // add a name to your badge
      description: "top 100 cow traders", // describe it !
      image: "cow_top_100.svg", // this is the svg path can be create easily from here https://factory.sismo.io/svg-editor
      publicContacts: [
        // give us a way to join you :)
        {
          type: "github", // github | twitter | lens ...
          contact: "leosayous21", // your username
        },
      ],
      eligibility: {
        // provide a short description of your eligibility criterias
        shortDescription: "Be a top 100 cow trader",
        // provide a technical description of your eligibility criterias
        specification:
          "You should have prevously create trades in the cow platform.",
      },
      links: [
        {
          logoUrl: "https://cow.fi/images/og-meta-cowprotocol.png", // a nice logo to have next to the url
          label: "COW", // label for your url
          url: "https://cow.fi/", 
        },
      ],
    },
```

![after-pressing-on-badge.png](after-pressing-on-badge.png)


## useful links:
[sismo docs](https://docs.sismo.io/sismo-docs/)
[create your own badge](https://factory.sismo.io/svg-editor)
