website : {
    name: "HelpingHandServer",
    prettyName: "Helping Hand",
    author: "John Carlyle, Jeremy Crowe, and Morgan McDermott",
    admins: { a : { name : "John Carlyle", email: "john.w.carlyle@gmail.com" },
	      b : { name: "Morgan McDermott", email: "morganmcdermott@gmail.com" },
	      c : { name: "Jeremy Crowe", email: "crowe.jb@gmail.com" }}
},

//some apps all up in this house
apps: {
    page: {
	models: {
	    //represents a single story
	    Item: {
		fields: {
		    title: CharField { length: 32 },
		    menu: CharField { length: 32 },
		    targetType: CharField { length: 32 },
		    target: CharField { length: 32, optional: "True" }
		},
		admin: "%title",
		listing: "<a id='%targetType%.%target%' href='#'>%title%</a>",
		display: "<a id='%targetType%.%target%' href='#'>%title%</a>"
	    },

	    Page: {
		fields: {
		    title: CharField { length: 32 },
		    content: TextField
		},
		admin: "%title",
		listing: "", //this should never come up
		display: "<h1>%title%</h1><div>%content%</div>"
	    }
	}
    }  
},

database: {
    name: "db.db",    
    engine: "django.db.backends.sqlite3"
},

menu: {
},

pages: {
    home: { title: "Homepage", url: "", template: "" },
    menu: { 
	title: "Menu", 
	url: "menu/(.*)/", 
	template: "%menuItems%", 
	menuItems: expr { expr: S[menu="%1"](page->Item) }
    },
    page: { 
	title: "Page", 
	url: "page/(.*)/", 
	template: "%pageData%", 
	pageData: expr { expr: S[title="%1"](page->Page) }
    }
}
