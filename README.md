# Notes

Based off https://themes.gohugo.io/themes/adritian-free-hugo-theme/

# Up And Running
 
 `hugo server -D`


# Todo

* Split ud i sider
* Kontakt i menuen -> side: Email, adresse/kort i s/h, tlf nummer?
* små ikoner ved nav-link? Tegnet, organisk, shamanistisk.
* Look: mere organisk, tegnet?
x make theme proper git submodule
* ny font
x nyt logo
x billeder af mig
% skifte nederste firkanter ud med skyer?
* farve i bund jordfarvet i stedet for sort
x knapper runde
% Ret bundtekst
    - link til th
x Ret menu
    - fjern Home
    - Yoga , Lydrejser , Meditationer , Om mig , Kontakt
x uddannelse
    - anatomy
    - openflow
    - simon krohn
    - s.k. meditation
    - hands on faye
x erfaring
    - dalgas 2021-nu
        . blid hatha flow
        . hatha
        . restorative
    - nor 2021-2022
        . Vinyasa
        . hatha
* kommende begivenheder
    - sverige ceremoni
    - lydrejse dalgas
* Behandlinger
    - Kommer snart!
* Struktur:
  sections = ["showcase", "upcoming-events", "yoga", "lydrejser", "meditationer", "om-mig", "erfaring", "uddannelse", "kontakt", "newsletter"]
* Colofon page? 
    - font, palette, date
    - Eagle photo credit: Photo by <a href="https://unsplash.com/@cadop?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mathew Schwartz</a> on <a href="https://unsplash.com/photos/bald-eagle-flying-on-skies-OjQgsR1oyEw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  

# Palette

From @AlexChristache No.35

    Glacial Ice (white)         #EAE9E7
    Chocolat (dark brown)       #782A2E
    Sunset Sienna (light brown) #B64D3C
    Angelic descent (yellow)    #EECC33
    Tile Blue (light blue)      #0094A5
    Blue Depths (dark blue)     #2C3A64

Text color:

html p.lead {
    color: #4A4A4A;
}

# Build and Deploy

Local dev: `hugo server -D`

Hosted on Cloudflare pages (free dns and hosting)

Build: `hugo`
Deploy: `npx wrangler pages deploy public --project-name indre-rn`

# Cloudflare setup

Set custom domain for pages: https://dash.cloudflare.com/f2946c09eeb0880bf7adf2790c4ae2b8/pages/view/indre-rn/domains  -> xn--indrern-u1a.dk

Must use non-ø version of domain. That creates a CNAME record, which points xn--indrern-u1a.dk -> indre-rn.pages.dev

