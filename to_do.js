let notion_token = <Your_notion_token>;

let notion_db_id = args.widgetParameter || args.queryParameters.parent_id
let req = new Request("https://api.notion.com/v1/databases/" + notion_db_id + "/query");
req.method = "POST";
req.headers = {
  'Authorization': 'Bearer ' + notion_token,
  'Notion-Version': '2021-08-16',
  'Content-Type': 'application/json'
};
  
req.body = JSON.stringify({
	  "filter": {
	    "or": [
	      {
	        "property": "State",
					"select": {
						"equals": "In Progress"
					}
	      },
	      {
	        "property": "State",
					"select": {
						"equals": "Open"
					}
				}
			]
		},
	  "sorts": [
	    {
	      "property": "Last edited time",
	      "direction": "ascending"
	    }
	  ]
  });

let res_body = await req.loadJSON()
App.close()

let widget = createWidget(res_body.results)
Script.setWidget(widget)
Script.complete()


function createWidget(res, widget_color, elements_color) {
  if (config.widgetFamily){
    switch(config.widgetFamily){
    case "small":
      limit = 3
      break;
    case "medium":
      limit = 5
      break;
    case "large":
      limit = 9
      break;
    }
  } else {
    limit = URLScheme.parameter("limit")
  }

  widget_color = "#202125"
  elements_color = Color.white()
      
  let w = new ListWidget()
    w.backgroundColor = new Color(widget_color)    
     w.addSpacer()
    
  for (let step = 0; step < res.length ; step++) {
    if (step == limit){
    break;
    }
  
    const doneTaskSymbol = SFSymbol.named("circle")
    let taskStack = w.addStack()
    const doneTask = taskStack.addImage(doneTaskSymbol.image)
    doneTask.imageSize = new Size(20, 20)
    doneTask.imageOpacity = 0.5
    doneTask.tintColor = elements_color
    doneTaskcontainerRelativeShape = true
    
    let cb_done_task = new CallbackURL("scriptable:///run/")
    cb_done_task.addParameter("scriptName", "task_done")
    cb_done_task.addParameter("token", notion_token)
    cb_done_task.addParameter("parent_id", notion_db_id.toString())
    cb_done_task.addParameter("limit", limit.toString())
    cb_done_task.addParameter("id", res[step].id.toString())
    doneTask.url = cb_done_task.getURL()

    taskStack.addSpacer(3)
    let taskName = taskStack.addText(res[step].properties.Name.title[0].text.content)
    taskName.textColor= elements_color
    taskName.textOpacity = 0.8
    taskName.font = Font.mediumSystemFont(16)
    taskStack.url = 'notion://' + res[step].url.replace(/(^\w+:|^)\/\//, '')
    
    if (step < limit - 1) {
      w.addSpacer()
    }
  }  

    w.url = 'notion://' + "www.notion.so/" + notion_db_id 
    
    const footerStack = w.addStack()


    const addTaskSymbol = SFSymbol.named("square.and.pencil")
    const addTask = footerStack.addImage(addTaskSymbol.image)
    addTask.imageSize = new Size(25, 25)
    addTask.tintColor = elements_color
    addTask.imageOpacity = 0.5
    let cb_addTask = new CallbackURL("scriptable:///run/")
    cb_addTask.addParameter("scriptName", "new_task")
    cb_addTask.addParameter("token", notion_token)
    cb_addTask.addParameter("parent_id", notion_db_id.toString())
    cb_addTask.addParameter("limit", limit.toString())
    addTask.url = cb_addTask.getURL()

    footerStack.addSpacer()
    
    const refreshStack = footerStack.addStack()
    refreshStack.url = "scriptable:///run?scriptName=to_do&limit=" + limit + "&parent_id=" + notion_db_id
    const refreshSymbol = SFSymbol.named("goforward")
    const refreshElement = refreshStack.addImage(refreshSymbol.image)
    refreshElement.imageSize = new Size(25, 25)
    refreshElement.tintColor = elements_color
    refreshElement.imageOpacity = 0.5
    
  return w;
} 
