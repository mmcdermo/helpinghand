//generate a webular site man
website : {
    name: "HelpingHandServer",
    prettyName: "Helping Hand",
    author: "John Carlyle, Jeremy Crowe, Morgan McDermott",
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
		    owner: CharField { length: 32 },
		    menu: CharField { length: 32, required: "false" },
		    page: ForeignKey { link: "'Page'", required: "false" }
		},
		admin: "%title",
		listing: "",
		display: ""
	    },

	    Page: {
		fields: {
		    title: CharField { length: 32 },
		    content: TextField
		},
		admin: "%title",
		listing: "",
		display: ""
	    }
	}
    }  
},

database: {
    name: "db.db",    
    engine: "django.db.backends.sqlite3"
},

menu: {
    home: { title: "Home", link: "/", placement: 0 }
},

pages: {
    home: { title: "dude", url: "/", template: "" }
}
