// Variables used by Scriptable.
// These must be at the very top of the file. Do not edit.
// icon-color: deep-blue; icon-glyph: book;

const NOTION_TOKEN = "<token>"

const timestamp = new Date().toLocaleTimeString()

// Determine the block URL (from various sources)
const blockUrl = args.shortcutParameter || args.widgetParameter

// Early exit, which triggers when used in the 'refresh' iOS Shortcut
// For some reason, this lets the widgets 'rerun' properly and update on command
if (!blockUrl) {
  Script.complete()
  return
}

// Determine block type and extract the correct ids from block URL
const collectionViewRegex = /\/(?<collectionId>\w+)\?v=(?<viewId>\w+$)/
const blockRegex = /\/.*?(?<blockId>\w+)$/
const collectionViewMatches = blockUrl.match(collectionViewRegex)
const blockMatches = blockUrl.match(blockRegex)
let blockType, collectionId, viewId, blockId
if (collectionViewMatches) {
  collectionId = collectionViewMatches.groups.collectionId
  viewId = collectionViewMatches.groups.viewId
  blockType = "collectionView"
} else {
  blockId = blockMatches.groups.blockId
  blockType = "block"
}

let widget = new ListWidget()
if (blockType === "block") {
  await applyBlockStyle(widget)
} else {
  await applyCollectionStyle(widget)
}

if (config.runsInWidget) {
  Script.setWidget(widget)
} else {
  widget.presentLarge()
}

Script.complete()

async function applyBlockStyle(widget) {
  const blockJson = await fetchBlock(blockId)

  addTitle(widget, blockJson["parent"]["title"], `notion://www.notion.so/${blockId}`)

  const childrenStack = widget.addStack()
  childrenStack.layoutVertically()
  blockJson["children"].forEach(childJson => {
    if (!("title" in childJson)) { return }
    addChildRow(childrenStack, childJson, "title")
  });

  // Push content to the top
  widget.addSpacer(null)

  if (!config.runsWithSiri) {
    addFooter(widget, `blocks/${blockId}/children`)
  }

  return widget
}

async function applyCollectionStyle() {
  const collectionViewJson = await fetchCollectionView(collectionId, viewId)

  addTitle(widget, collectionViewJson["collection"]["collection_title"], `notion://www.notion.so/${collectionId}?v=${viewId}`)

  const childrenStack = widget.addStack()
  childrenStack.layoutVertically()
  collectionViewJson["rows"].forEach(childJson => {
    if (!("name" in childJson)) { return }
    addChildRow(childrenStack, childJson, "name")
  });

  // Push content to the top
  widget.addSpacer(null)

  if (!config.runsWithSiri) {
    addFooter(widget, `collections/${collectionId}/${viewId}`)
  }

  return widget
}

function addChildRow(childrenStack, childJson, textKey) {
  if (!childJson[textKey]) { return }

  childStack = childrenStack.addStack()
  childStack.centerAlignContent()

  const deleteSymbol = SFSymbol.named("trash.fill")
  const deleteElement = childStack.addImage(deleteSymbol.image)
  deleteElement.imageSize = new Size(16, 16)
  deleteElement.tintColor = Color.white()
  deleteElement.imageOpacity = 0.75
  deleteElement.url = `shortcuts://run-shortcut?name=Delete%20Notion%20Block&input=${childJson["id"]}`

  childStack.addSpacer(8)

  const titleElement = childStack.addText(childJson[textKey])
  titleElement.textColor = Color.white()
  titleElement.font = Font.mediumSystemFont(16)
  titleElement.minimumScaleFactor = 0.75
  titleElement.url = `notion://www.notion.so/${childJson["id"]}`

  childrenStack.addSpacer(8)
}

function addTitle(widget, title, url) {
  const titleStack = widget.addStack()
  titleStack.url = url
  titleStack.centerAlignContent()

  const linkSymbol = SFSymbol.named("arrow.up.right.square.fill")
  const linkElement = titleStack.addImage(linkSymbol.image)
  linkElement.imageSize = new Size(16, 16)
  linkElement.tintColor = Color.white()

  titleStack.addSpacer(6)

  const titleElement = titleStack.addText(title)
  titleElement.textColor = Color.white()
  titleElement.font = Font.boldSystemFont(18)
  titleElement.minimumScaleFactor = 0.75
  widget.addSpacer(6)
}

function addFooter(widget, addUrlPath) {
    const footerStack = widget.addStack()
    footerStack.bottomAlignContent()

    const addSymbol = SFSymbol.named("plus.square.fill")
    const addElement = footerStack.addImage(addSymbol.image)
    addElement.imageSize = new Size(20, 20)
    addElement.tintColor = Color.white()
    addElement.url = `shortcuts://run-shortcut?name=Append%20to%20Notion%20Block&input=${addUrlPath}`

    footerStack.addSpacer(null)

    const refreshStack = footerStack.addStack()
    refreshStack.url = `shortcuts://run-shortcut?name=Refresh%20Notion%20Block&input=${blockUrl}`
    refreshStack.centerAlignContent()

    const refreshSymbol = SFSymbol.named("arrow.clockwise.icloud.fill")
    const refreshElement = refreshStack.addImage(refreshSymbol.image)
    refreshElement.imageSize = new Size(20, 20)
    refreshElement.tintColor = Color.white()

    refreshStack.addSpacer(5)

    const updatedAtElement = refreshStack.addText(`Last Sync: ${timestamp}`)
    updatedAtElement.textColor = Color.white()
    updatedAtElement.textOpacity = 0.6
    updatedAtElement.font = Font.mediumSystemFont(10)
}

async function fetchBlock(blockId) {
  const request = notionServerRequest(`https://notion-server.herokuapp.com/blocks/${blockId}/children`)
  return await request.loadJSON()
}

async function fetchCollectionView(collectionId, viewId) {
  const request = notionServerRequest(`https://notion-server.herokuapp.com/collections/${collectionId}/${viewId}`)
  return await request.loadJSON()
}

function notionServerRequest(url) {
  const request = new Request(url)
  request.method = 'GET'
  request.headers = {
    'Notion-Token': NOTION_TOKEN
  }

  return request
}
