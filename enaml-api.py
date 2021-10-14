#!/usr/bin/env python3
# coding: utf-8
# naming: pep-0008
# typing: pep-0484
# docstring: pep-0257
# indentation: tabulation (4 spc)

""" enaml-api.py
	API list in copy/paste friendly format
"""

# How to use this file

# This file is *not* runnable
# This file is *not* an exhaustive documentation
# This file briefly describes the topology of the module
# This file briefly describes the different classes
# This file briefly describes the relationship between classes
# Check the 'Dependencies and relationship' part below
# Copy and paste the 'from ... import ...' and 'xxx:' parts into the enaml file
# Ensure relationship is preserved, indent as needed, adapt members and methods
# Check often using 'enaml-run file.enaml'

# Hierarchy and inheritance

#	(atom)			(Atom)
#	widgets			+--	Border
#					|		style = Enum('box', 'panel', 'styled_panel')
#					|		line_style = Enum('plain', 'sunken', 'raised')
#					|		line_width = Range(low=0, value=1)
#					|		midline_width = Range(low=0, value=0)
#	(enamlx)		+--	Brush
#					+--	CloseEvent
#					|	self.is_accepted()
#					|	self.accept()
#					|	self.ignore()
#					+--	ConstraintHelper
#					|	|	strength = StrengthMember()
#					|	|	#
#					|	|	self.__or__(strength)
#					|	|	self.when(switch)
#					|	|	self.create_constraints(component)
#					|	|	self.constraints(component)
#					|	+--	BoxHelper
#					|	|	|	self.box_constraints(component)
#					|	|	+--	LinearBoxHelper
#					|	|			orientation = Enum('vertical', 'horizontal')
#					|	|			items = Tuple()
#					|	|			spacing = Range(low=0)
#					|	|			margins = Coerced(Box)
#					|	|			items = Tuple()
#					|	|			#
#					|	|			cls.validate(items)
#					|	|			#
#					|	|			self.__init__(orientation, items, spacing=10, margins=0)
#					|	|			self.constraints(component)
#					|	+--	FactoryHelper
#					|	|		factory = Callable()
#					|	|		args = Tuple()
#					|	|		kwargs = Dict()
#					|	|		#
#					|	|		self.__init__(factory, *args, **kwargs)
#					|	|		self.constraints(component)
#					|	+--	GridHelper
#					|	|		rows = Tuple()
#					|	|		row_align = Str()
#					|	|		row_spacing = Range(low=0)
#					|	|		column_align = Str()
#					|	|		column_spacing = Range(low=0)
#					|	|		margins = Coerced(Box)
#					|	|		#
#					|	|		cls.validate(rows)
#					|	|		#
#					|	|		self.__init__(rows, **config)
#					|	|		self.constraints(component)
#					|	+--	SequenceHelper
#					|			first_name = Str()
#					|			second_name = Str()
#					|			items = Tuple()
#					|			spacing = Range(low=0)
#					|			#
#					|			cls.validate(items)
#					|			#
#					|			self.__init__(first_name, second_name, items, spacing=10)
#					|			self.constraints(component)
#					+--	DockEvent
#					|	+--	DockItemEvent
#					|			Docked
#					|			Undocked
#					|			Extended
#					|			Retracted
#					|			Shown
#					|			Hidden
#					|			Closed
#					|			TabSelected
#					|			#
#					|			type = Typed(Type)
#					|			name = Str()
#					+--	DockLayoutOp
#	layout			|	+--	ExtendItem
#					|	|		item = Str()
#	layout			|	+--	FloatArea
#					|	|		area = Coerced(AreaLayout)
#	layout			|	+--	FloatItem
#					|	|		item = Coerced(ItemLayout)
#	layout			|	+--	InsertBorderItem
#					|	|		item = Str()
#					|	|		target = Str()
#					|	|		position = Enum('left', 'top', 'right', 'bottom')
#	layout			|	+--	InsertDockBarItem
#					|	|		item = Str()
#					|	|		target = Str()
#					|	|		position = Enum('right', 'left', 'bottom', 'top')
#					|	|		index = Int(-1)
#	layout			|	+--	InsertItem
#					|	|		item = Str()
#					|	|		target = Str()
#					|	|		position = Enum('left', 'top', 'right', 'bottom')
#	layout			|	+--	InsertTab
#					|	|		item = Str()
#					|	|		target = Str()
#					|	|		index = Int(-1)
#					|	|		tab_position = Enum('default', 'top', 'bottom', 'left', 'right')
#	layout			|	+--	RemoveItem
#					|	|		item = Str()
#	layout			|	+--	RetractItem
#					|			item = Str()
#					+--	DragData
#					|		mime_data = Typed(MimeData, factory=mime_data_factory)
#					|		default_drop_action = Coerced(DropAction, (DropAction.Ignore,))
#					|		supported_actions = Coerced(DropAction.Flags, (DropAction.Move,))
#					|		image = Typed(Image)
#					|		hotspot = Tuple(item=Int())
#					+--	DropEvent
#					|		self.drop_action()
#					|		self.ignore()
#					|		self.is_accepted()
#					|		self.mime_data()
#					|		self.pos()
#					|		self.possible_actions()
#					|		self.proposed_action()
#					|		self.set_accepted(accepted)
#					|		self.set_drop_action(action)
#					+--	Icon
#					|		>IconImage
#					|		images = List(IconImage)
#					+--	IconImage
#					|		mode = Enum('normal', 'active', 'disabled', 'selected')
#					|		state = Enum('off', 'on')
#					|		image = Typed(Image)
#					+--	Image
#					|		format = Enum('auto', 'png', 'jpg', 'gif', 'bmp', 'xpm', 'xbm', 'pbm', 'pgm', 'ppm', 'tiff', 'argb32')
#					|		raw_size = Coerced(Size, (0, 0))
#					|		size = Coerced(Size, (-1, -1))
#					|		aspect_ratio_mode = Enum('ignore', 'keep', 'keep_by_expanding')
#					|		transform_mode = Enum('smooth', 'fast')
#					|		data = Bytes()
#					+--	LayoutItem
#					|		self.__call__()
#					|		self.hard_constraints()
#					|		self.margin_constraints()
#					|		self.geometry_constraints()
#					|		layout_constraints => ():
#					|		self.constrainable()
#					|		self.constraints()
#					|		self.margins()
#					|		self.size_hint()
#					|		self.min_size()
#					|		self.max_size()
#					|		self.set_geometry()
#					+--	LayoutManager
#					|		self.__init__(item)
#					|		self.set_items(item)
#					|		self.clear_items()
#					|		self.resize(width, height)
#					|		self.best_size()
#					|		self.min_size()
#					|		self.max_size()
#					|		self.update_geometry(index)
#					|		self.update_margins(index)
#					+--	LayoutNode
#					|	|	self.children()
#					|	|	self.traverse(depth_first=False)
#					|	|	self.find(kind)
#					|	|	self.find_all(kind)
#	layout			|	+--	AreaLayout
#					|	|		items = Coerced(_AreaLayoutItem)
#					|	|		dock_bars = List(DockBarLayout)
#					|	|		floating = Bool(False)
#					|	|		geometry = Coerced(Rect, (-1, -1, -1, -1), coercer=_coerce_rect)
#					|	|		linked = Bool(False)
#					|	|		maximized = Bool(False)
#					|	|		#
#					|	|		self.__init__(item=None, **kwargs)
#					|	|		self.children()
#	layout			|	+--	DockBarLayout
#					|	|		position = Enum('top', 'right', 'bottom', 'left')
#					|	|		items = List(Coerced(ItemLayout))
#					|	|		#
#					|	|		self.__init__(*items, **kwargs)
#					|	|		self.children()
#	layout			|	+--	DockLayout
#					|	|		items = List(Coerced(_DockLayoutItem))
#					|	|		#
#					|	|		self.__init__(*items, **kwargs)
#					|	|		self.children()
#					|	+--	(NodeVisitor)
#					|	|	+--	DockLayoutValidator
#					|	|			self.__init__(available)
#					|	|			self.warn(message)
#					|	|			self.setup(node)
#					|	|			self.teardown(node)
#					|	|			self.visit_ItemLayout(node)
#					|	|			self.visit_TabLayout(node)
#					|	|			self.visit_SplitLayout(node)
#					|	|			self.visit_DockBarLayout(node)
#					|	|			self.visit_AreaLayout(node)
#					|	|			self.visit_DockLayout(node)
#					|	+--	(UserWarning)
#	layout			|	|	+--	DockLayoutWarning
#	layout			|	+--	ItemLayout
#					|	|		name = Str()
#					|	|		floating = Bool(False)
#					|	|		geometry = Coerced(Rect, (-1, -1, -1, -1), coercer=_coerce_rect)
#					|	|		linked = Bool(False)
#					|	|		maximized = Bool(False)
#					|	|		#
#					|	|		self.__init__(name, **kwargs)
#	layout			|	+--	SplitLayout
#					|	|	|	orientation = Enum('horizontal', 'vertical')
#					|	|	|	sizes = List(Int())
#					|	|	|	items = List(Coerced(_SplitLayoutItem))
#					|	|	|	#
#					|	|	|	self.__init__(*items, **kwargs)
#					|	|	|	self.children()
#	layout			|	|	+--	HSplitLayout
#					|	|	|		self.__init__(*items, **kwargs)
#	layout			|	|	+--	VSplitLayout
#					|	|			self.__init__(*items, **kwargs)
#	layout			|	+--	TabLayout
#					|			tab_position = Enum('top', 'bottom', 'left', 'right')
#					|			index = Int(0)
#					|			maximized = Bool(False)
#					|			items = List(Coerced(ItemLayout))
#					|			#
#					|			self.__init__(*items, **kwargs)
#					|			self.children()
#					+--	LiveEditorModel
#					|		model_text = Str()
#					|		view_text = Str()
#					|		model_item = Str()
#					|		view_item = Str()
#					|		model_filename = Str()
#					+--	MimeData
#					|		self.formats()
#					|		self.has_format(mime_type)
#					|		self.remove_format(mime_type)
#					|		self.data(mime_type)
#					|		self.set_data(mime_type, data)
#	core			+--	Object
#					|	|	name = Str()
#					|	|	parent = Object()
#					|	|	children = List(Object())
#					|	|	is_destroyed = flag_property(DESTROYED_FLAG)
#					|	|	destroyed :: Event()
#					|	|	#
#					|	|	parent_changed => (old, new):
#					|	|	child_added => (child):
#					|	|	child_moved => (child):
#					|	|	child_removed => (child):
#					|	|	#
#					|	|	self.destroy()
#					|	|	self.set_parent(parent)
#					|	|	self.insert_children(before, insert)
#					|	|	self.root_object()
#					|	|	self.traverse(depth_first=False)
#					|	|	self.traverse_ancestors(root=None)
#					|	|	self.find(name, regex=False)
#					|	|	self.find_all(name, regex=False)
#	core			|	+--	Declarative
#					|		|	name = Str()
#					|		|	initialized :: Event()
#					|		|	is_initialized = flag_property()
#					|		|	#
#					|		|	self.initialize()
#					|		|	self.destroy()
#					|		|	self.child_added(child)
#	workbench.ui	|		+--	ActionItem
#					|		|		path = Str()
#					|		|		group = Str()
#					|		|		before = Str()
#					|		|		after = Str()
#					|		|		command = Str()
#					|		|		parameters = Dict()
#					|		|		label = Str()
#					|		|		shortcut = Str()
#					|		|		visible = Bool(True)
#					|		|		enabled = Bool(True)
#					|		|		checkable = Bool(False)
#					|		|		checked = Bool(False)
#					|		|		icon = Typed(Icon)
#					|		|		tool_tip = Str()
#					|		|		status_tip = Str()
#	workbench.ui	|		+--	Autostart
#					|		|		plugin_id = Str()
#	workbench.ui	|		+--	Branding
#					|		|		title = Str()
#					|		|		icon = Typed(Icon)
#	workbench.core	|		+--	Command
#					|		|		id = Str()
#					|		|		description = Str()
#					|		|		handler = Callable(ExecutionEvent)
#	core			|		+--	DynamicTemplate
#					|		|		<Container
#					|		|		base = Typed(Template)
#					|		|		args = Tuple()
#					|		|		tags = Tuple(Str())
#					|		|		startag = Str()
#					|		|		data = Dict()
#					|		|		tagged = Typed(ObjectDict, ())
#					|		|		#
#					|		|		self.initialize()
#					|		|		self.destroy()
#	workbench		|		+--	Extension
#					|		|		id = Str()
#					|		|		point = Str()
#					|		|		rank = Int()
#					|		|		factory = Callable()
#					|		|		description = Str()
#					|		|		#
#					|		|		self.plugin_id
#					|		|		self.qualified_id
#					|		|		#
#					|		|		self.get_child(kind, reverse=False)
#					|		|		self.get_children(kind)
#	workbench		|		+--	ExtensionPoint
#					|		|		<PluginManifest
#					|		|		id = Str()
#					|		|		extensions = Tuple()
#					|		|		description = Str()
#					|		|		#
#					|		|		self.plugin_id
#					|		|		self.qualified_id
#	core			|		+--	Include
#					|		|	|	<Container
#					|		|	|	objects = ContainerList(Object)
#					|		|	|	destroy_old = Bool(True)
#					|		|	|	#
#					|		|	|	self.initialize()
#					|		|	|	self.destroy()
#	(stdlib)		|		|	+--	MappedView
#	workbench.ui	|		+--	ItemGroup
#					|		|		id = Str()
#					|		|		visible = Bool(True)
#					|		|		enabled = Bool(True)
#					|		|		exclusive = Bool(False)
#	workbench.ui	|		+--	MenuItem
#					|		|		path = Str()
#					|		|		group = Str()
#					|		|		before = Str()
#					|		|		after = Str()
#					|		|		label = Str()
#					|		|		visible = Bool(True)
#					|		|		enabled = Bool(True)
#					|		|		#
#					|		|		self.item_groups = List(ItemGroup)
#					|		+--	Pattern
#					|		|	|	self.destroy()
#					|		|	|	self.child_node_intercept(nodes, key, f_locals)
#					|		|	|	self.pattern_items()
#	core			|		|	+--	Conditional
#					|		|	|		>Container
#					|		|	|		condition = Bool()
#					|		|	|		#
#					|		|	|		self.destroy()
#					|		|	|		self.pattern_items()
#					|		|	|		self.refresh_items()
#	core			|		|	+--	Looper
#					|		|			>Container
#					|		|			iterable = Coerced(LooperIterable)
#					|		|			items = List()
#					|		|			#
#					|		|			loop_index
#					|		|			loop_item
#					|		|			loop.index
#					|		|			loop.item
#					|		|			#
#					|		|			self.destroy()
#					|		|			self.pattern_items()
#					|		|			self.refresh_items()
#	workbench		|		+--	PluginManifest
#					|		|		>ExtensionPoint
#					|		|		id = Str()
#					|		|		factory = Callable(plugin_factory) -> Plugin
#					|		|		workbench = ForwardTyped(Workbench)
#					|		|		description = Str()
#					|		|		#
#					|		|		self.extensions = List(Extension())
#					|		|		self.extension_points = List(ExtensionPoint())
#					|		+--	Setter
#					|		|		field = Str()
#					|		|		value = Str()
#					|		|		#
#					|		|		self.destroy()
#	(stdlib)		|		+--	SliderTransform
#					|		|	|	minimum = Value()
#					|		|	|	maximum = Value()
#					|		|	|	value = Value()
#					|		|	|	#
#					|		|	|	self.get_minimum()
#					|		|	|	self.get_maximum()
#					|		|	|	self.get_value()
#					|		|	|	self.set_value(value)
#	(stdlib)		|		|	+--	FloatTransform
#					|		|			minimum = Float(0.0)
#					|		|			maximum = Float(1.0)
#					|		|			value = Float(0.0)
#					|		|			precision = Range(low=1, value=100)
#					|		|			#
#					|		|			self.get_minimum()
#					|		|			self.get_maximum()
#					|		|			self.get_value()
#					|		|			self.set_value(val)
#					|		+--	Stylable
#					|		|		style_class = Str()
#					|		|		#
#					|		|		self.destroy()
#					|		|		self.style_sheet()
#					|		|		self.restyle()
#					|		|		self.parent_changed(old, new)
#					|		|		self.child_added(child)
#					|		|		self.child_removed(child)
#					|		+--	Style
#					|		|		element = Str()
#					|		|		style_class = Str()
#					|		|		object_name = Str()
#					|		|		pseudo_class = Str()
#					|		|		pseudo_element = Str()
#					|		|		#
#					|		|		self.setters()
#					|		|		self.match(item)
#					|		|		self.destroy()
#					|		|		self.child_added(child)
#					|		|		self.child_removed(child)
#					|		+--	StyleSheet
#					|		|	|	self.destroy()
#					|		|	|	self.styles()
#					|		|	|	self.child_added(child)
#					|		|	|	self.child_removed(child)
#	(stdlib)		|		|	+--	TaskDialogStyleSheet
#					|		+--	ToolkitObject
#					|		|	|	activated = d_(Event(), writable=False)
#					|		|	|	proxy = Typed(ProxyToolkitObject)
#					|		|	|	proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
#					|		|	|	#
#					|		|	|	self.initialize()
#					|		|	|	self.destroy()
#					|		|	|	self.child_added(child)
#					|		|	|	self.child_removed(child)
#					|		|	|	self.activate_proxy()
#					|		|	|	self.activate_top_down()
#					|		|	|	self.activate_bottom_up()
#	widgets			|		|	+--	Action
#					|		|	|	|	<ActionGroup
#					|		|	|	|	<Menu
#					|		|	|	|	<ToolBar
#					|		|	|	|	text = Str()
#					|		|	|	|	tool_tip = Str()
#					|		|	|	|	status_tip = Str()
#					|		|	|	|	icon = Typed(Icon)
#					|		|	|	|	checkable = Bool(False)
#					|		|	|	|	checked = Bool(False)
#					|		|	|	|	enabled = Bool(True)
#					|		|	|	|	visible = Bool(True)
#					|		|	|	|	separator = Bool(False)
#					|		|	|	|	triggered :: Event(bool)
#					|		|	|	|	toggled :: Event(bool)
#					|		|	|	|	proxy = Typed(ProxyAction)
#					|		|	|	+--	WorkbenchAction
#	widgets			|		|	+--	ActionGroup
#					|		|	|	|	<Menu
#					|		|	|	|	<ToolBar
#					|		|	|	|	>Action
#					|		|	|	|	exclusive = Bool(True)
#					|		|	|	|	enabled = Bool(True)
#					|		|	|	|	visible = Bool(True)
#					|		|	|	|	proxy = Typed(ProxyActionGroup)
#					|		|	|	|	#
#					|		|	|	|	self.actions()
#					|		|	|	+--	WorkbenchActionGroup
#	widgets			|		|	+--	ButtonGroup
#					|		|	|		<Container
#					|		|	|		group_members = Typed(set, ())
#					|		|	|		exclusive = Bool(True)
#					|		|	|		proxy = Typed(ProxyButtonGroup)
#	widgets			|		|	+--	FileDialog
#					|		|	|		:FileDialogEx
#					|		|	|		title = Str()
#					|		|	|		mode = Enum('open_file', 'open_files', 'save_file', 'directory')
#					|		|	|		path = Str()
#					|		|	|		paths = List(Str())
#					|		|	|		filters = List(Str())
#					|		|	|		selected_filter = Str()
#					|		|	|		native_dialog = Bool(True)
#					|		|	|		result = Enum('rejected', 'accepted')
#					|		|	|		callback = Callable()
#					|		|	|		accepted :: Event(str)
#					|		|	|		rejected :: Event()
#					|		|	|		closed :: Event()
#					|		|	|		destroy_on_close = Bool(True)
#					|		|	|		proxy = Typed(ProxyFileDialog)
#					|		|	|		#
#					|		|	|		self.open()
#					|		|	|		self.exec_()
#	widgets			|		|	+--	FocusTracker
#					|		|	|		focused_widget = Typed(Widget)
#					|		|	|		proxy = Typed(ProxyFocusTracker)
#	(enamlx)		|		|	+--	GraphicsItem
#	(enamlx)		|		|	|	|	<GraphicsView
#	(enamlx)		|		|	|	+--	AbstractGraphicsShapeItem
#	(enamlx)		|		|	|	|	+--	GraphicsEllipseItem
#	(enamlx)		|		|	|	|	+--	GraphicsLineItem
#	(enamlx)		|		|	|	|	+--	GraphicsPathItem
#	(enamlx)		|		|	|	|	+--	GraphicsPolygonItem
#	(enamlx)		|		|	|	|	+--	GraphicsRectItem
#	(enamlx)		|		|	|	|	+--	GraphicsTextItem
#	(enamlx)		|		|	|	+--	GraphicsImageItem
#	(enamlx)		|		|	|	+--	GraphicsItemGroup
#	(enamlx)		|		|	|	+--	GraphicsWidget
#	widgets			|		|	+--	Menu
#					|		|	|	|	<MenuBar
#					|		|	|	|	>Action
#					|		|	|	|	>ActionGroup
#					|		|	|	|	<Menu
#					|		|	|	|	>Menu
#					|		|	|	|	title = Str()
#					|		|	|	|	enabled = Bool(True)
#					|		|	|	|	visible = Bool(True)
#					|		|	|	|	context_menu = Bool(False)
#					|		|	|	|	proxy = Typed(ProxyMenuBar)
#					|		|	|	|	#
#					|		|	|	|	self.items()
#					|		|	|	|	self.popup()
#					|		|	|	|	self.close()
#					|		|	|	+--	WorkbenchMenu
#	widgets			|		|	+--	MenuBar
#					|		|	|		<MainWindow
#					|		|	|		<Widget
#					|		|	|		>Menu
#					|		|	|		proxy = Typed(ProxyMenuBar)
#					|		|	|		#
#					|		|	|		self.menus()
#	widgets			|		|	+--	StatusItem
#					|		|	|		<StatusBar
#					|		|	|		>WIDGETS
#					|		|	|		time_format = Enum('normal', 'permanent')
#					|		|	|		stretch = Range(low=0)
#					|		|	|		proxy = Typed(ProxyStatusItem)
#					|		|	|		#
#					|		|	|		self.status_widget()
#	widgets			|		|	+--	Timer
#					|		|	|		interval = Int(0)
#					|		|	|		single_shot = Bool(False)
#					|		|	|		timeout :: Event()
#					|		|	|		proxy = Typed(ProxyTimer)
#					|		|	|		#
#					|		|	|		self.start()
#					|		|	|		self.stop()
#					|		|	|		self.is_active()
#					|		|	+--	ToolkitDialog
#					|		|	|	|	title = d_(Str())
#					|		|	|	|	callback = d_(Callable())
#					|		|	|	|	destroy_on_close = d_(Bool(True))
#					|		|	|	|	accepted = d_(Event(), writable=False)
#					|		|	|	|	rejected = d_(Event(), writable=False)
#					|		|	|	|	finished = d_(Event(bool), writable=False)
#					|		|	|	|	result = Bool(False)
#					|		|	|	|	proxy = Typed(ProxyToolkitDialog)
#					|		|	|	|	#
#					|		|	|	|	self.show()
#					|		|	|	|	self.open()
#					|		|	|	|	self.exec_()
#					|		|	|	|	self.accept()
#					|		|	|	|	self.reject()
#	widgets			|		|	|	+--	ColorDialog
#					|		|	|	|		current_color = ColorMember('white')
#					|		|	|	|		show_alpha = Bool(True)
#					|		|	|	|		show_buttons = Bool(True)
#					|		|	|	|		selected_color = ColorMember()
#					|		|	|	|		proxy = Typed(ProxyColorDialog)
#					|		|	|	|		#
#					|		|	|	|		cls.get_color(parent=None, **kwargs)
#					|		|	|	|		cls.custom_count()
#					|		|	|	|		cls.custom_color(index)
#					|		|	|	|		cls.set_custom_color(index, color)
#	widgets			|		|	|	+--	FileDialogEx
#					|		|	|			:FileDialog
#					|		|	|			file_mode = Enum('any_file', 'existing_file', 'existing_files', 'directory')
#					|		|	|			show_dirs_only = Bool(False)
#					|		|	|			current_path = Str()
#					|		|	|			selected_paths = List(Str())
#					|		|	|			name_filters = List(Str())
#					|		|	|			selected_name_filter = Str()
#					|		|	|			proxy = Typed(ProxyFileDialogEx)
#					|		|	|			#
#					|		|	|			cls.get_existing_directory(parent=None, **kwargs)
#					|		|	|			cls.get_open_file_name(parent=None, **kwargs)
#					|		|	|			cls.get_open_file_names(parent=None, **kwargs)
#					|		|	|			cls.get_save_file_name(parent=None, **kwargs)
#					|		|	|			#
#					|		|	|			self.exec_native()
#					|		|	+--	Widget
#					|		|		|	enabled = Bool(True)
#					|		|		|	visible = Bool(True)
#					|		|		|	background = ColorMember()
#					|		|		|	foreground = ColorMember()
#					|		|		|	font = FontMember()
#					|		|		|	minimum_size = Coerced(Size, (-1, -1))
#					|		|		|	maximum_size = Coerced(Size, (-1, -1))
#					|		|		|	tool_tip = Str()
#					|		|		|	status_tip = Str()
#					|		|		|	features = Coerced(Feature.Flags)
#					|		|		|	proxy = Typed(ProxyWidget)
#					|		|		|	#
#					|		|		|	self.restyle()
#					|		|		|	self.show(s)
#					|		|		|	self.hide()
#					|		|		|	#
#					|		|		|	next_focus_child => (current):
#					|		|		|	previous_focus_child => (current):
#					|		|		|	focus_gained => ():
#					|		|		|	focus_lost => ():
#					|		|		|	drag_start => ():
#					|		|		|	drag_end => (drag_data, result):
#					|		|		|	drag_enter => (event):
#					|		|		|	drag_move => (event):
#					|		|		|	drag_leave => ():
#					|		|		|	drop => (event):
#					|		|		+--	ConstraintsWidget
#					|		|		|	|	<Container
#					|		|		|	|	constraints = List()
#					|		|		|	|	hug_width = PolicyEnum('strong')
#					|		|		|	|	hug_height = PolicyEnum('strong')
#					|		|		|	|	resist_width = PolicyEnum('strong')
#					|		|		|	|	resist_height = PolicyEnum('strong')
#					|		|		|	|	limit_width = PolicyEnum('ignore')
#					|		|		|	|	limit_height = PolicyEnum('ignore')
#					|		|		|	|	proxy = Typed(ProxyConstraintsWidget)
#					|		|		|	|	#
#					|		|		|	|	self.request_relayout()
#					|		|		|	|	self.when(switch)
#					|		|		|	|	layout_constraints => ():
#					|		|		|	+--	Control
#					|		|		|	|	|	proxy = Typed(ProxyControl)
#					|		|		|	|	+--	AbstractButton
#					|		|		|	|	|	|	text = Str()
#					|		|		|	|	|	|	icon = Typed(Icon)
#					|		|		|	|	|	|	icon_size = Coerced(Size, (-1, -1))
#					|		|		|	|	|	|	group = ForwardTyped(ButtonGroup)
#					|		|		|	|	|	|	checkable = Bool(False)
#					|		|		|	|	|	|	checked = Bool(False)
#					|		|		|	|	|	|	clicked :: Event(bool)
#					|		|		|	|	|	|	toggled :: Event(bool)
#					|		|		|	|	|	|	hug_width = set_default('weak')
#					|		|		|	|	|	|	proxy = Typed(ProxyAbstractButton)
#					|		|		|	|	|	|	#
#					|		|		|	|	|	|	self.__init__(parent=None, **kwargs)
#	widgets			|		|		|	|	|	+--	CheckBox
#					|		|		|	|	|	|		<Container
#					|		|		|	|	|	|		checkable = Bool(True)
#					|		|		|	|	|	|		proxy = Typed(ProxyCheckBox)
#	widgets			|		|		|	|	|	+--	PushButton
#					|		|		|	|	|	|		<Container
#					|		|		|	|	|	|		>(Menu)
#					|		|		|	|	|	|		default = Bool(False)
#					|		|		|	|	|	|		proxy = Typed(ProxyPushButton)
#					|		|		|	|	|	|		#
#					|		|		|	|	|	|		self.menu()
#	widgets			|		|		|	|	|	+--	RadioButton
#					|		|		|	|	|	|		<Container
#					|		|		|	|	|	|		checkable = set_default(True)
#					|		|		|	|	|	|		proxy = Typed(ProxyRadioButton)
#	widgets			|		|		|	|	|	+--	ToolButton
#					|		|		|	|	|			<ToolBar
#					|		|		|	|	|			<(Container)
#					|		|		|	|	|			>(Menu)
#					|		|		|	|	|			button_style = Enum('icon_only', 'text_only', 'text_beside_icon', 'text_under_icon')
#					|		|		|	|	|			auto_raise = Bool(True))
#					|		|		|	|	|			popup_mode = Enum('delayed', 'button', 'instant')
#					|		|		|	|	|			proxy = Typed(ProxyToolButton)
#	(enamlx)		|		|		|	|	+--	AbstractItemView
#	(enamlx)		|		|		|	|	|	+--	TableView
#	(enamlx)		|		|		|	|	|	+--	TreeView
#	(enamlx)		|		|		|	|	+--	AbstractWidgetItemGroup
#	(enamlx)		|		|		|	|	|	|	>AbstractWidgetItem
#	(enamlx)		|		|		|	|	|	+--	AbstractWidgetItem
#	(enamlx)		|		|		|	|	|	|	+--	TableViewItem
#	(enamlx)		|		|		|	|	|	|	+--	TreeViewItem
#	(enamlx)		|		|		|	|	|	|	|		<TreeViewItem
#	(enamlx)		|		|		|	|	|	|	|		>TreeViewItem
#	(enamlx)		|		|		|	|	|	|	+--	TreeViewColumn
#	(enamlx)		|		|		|	|	|	+--	TableViewRow
#	(enamlx)		|		|		|	|	|	+--	TableViewColumn
#					|		|		|	|	+--	BoundedDate
#					|		|		|	|	|	|	minimum = Typed(pydate, args=(1752, 9, 14))
#					|		|		|	|	|	|	maximum = Typed(pydate, args=(7999, 12, 31))
#					|		|		|	|	|	|	date = Typed(pydate, factory=pydate.today)
#					|		|		|	|	|	|	proxy = Typed(ProxyBoundedDate)
#	widgets			|		|		|	|	|	+--	Calendar
#					|		|		|	|	|	|		<Container
#					|		|		|	|	|	|		:DateSelector
#					|		|		|	|	|	|		:DatetimeSelector
#					|		|		|	|	|	|		proxy = Typed(ProxyCalendar)
#	widgets			|		|		|	|	|	+--	DateSelector
#					|		|		|	|	|			<Container
#					|		|		|	|	|			:Calendar
#					|		|		|	|	|			date_format = Str()
#					|		|		|	|	|			calendar_popup = Bool(False)
#					|		|		|	|	|			hug_width = set_default('ignore')
#					|		|		|	|	|			proxy = Typed(ProxyDateSelector)
#					|		|		|	|	+--	BoundedDatetime
#					|		|		|	|	|	|	minimum = Typed(pydatetime, args=(1752, 9, 14, 0, 0, 0, 0))
#					|		|		|	|	|	|	maximum = Typed(pydatetime, args=(7999, 12, 31, 23, 59, 59, 999000))
#					|		|		|	|	|	|	datetime = Typed(pydatetime, factory=pydatetime.now)
#					|		|		|	|	|	|	proxy = Typed(ProxyBoundedDatetime)
#	widgets			|		|		|	|	|	+--	DatetimeSelector
#					|		|		|	|	|			<Container
#					|		|		|	|	|			:Calendar
#					|		|		|	|	|			datetime_format = Str()
#					|		|		|	|	|			calendar_popup = Bool(False)
#					|		|		|	|	|			hug_width = set_default('ignore')
#					|		|		|	|	|			proxy = Typed(ProxyDatetimeSelector)
#					|		|		|	|	+--	BoundedTime
#					|		|		|	|	|	|	minimum = Typed(pytime, args=(0, 0, 0))
#					|		|		|	|	|	|	maximum = Typed(pytime, args=(23, 59, 59, 999000))
#					|		|		|	|	|	|	time = Typed(pytime, factory=lambda: datetime.now().time())
#					|		|		|	|	|	|	proxy = Typed(ProxyBoundedTime)
#	widgets			|		|		|	|	|	+--	TimeSelector
#					|		|		|	|	|			<Container
#					|		|		|	|	|			time_format = Str()
#					|		|		|	|	|			hug_width = set_default('ignore')
#					|		|		|	|	|			proxy = Typed(ProxyTimeSelector)
#	widgets			|		|		|	|	+--	ComboBox
#					|		|		|	|	|		<Container
#					|		|		|	|	|		:ObjectCombo
#					|		|		|	|	|		items = List(Str())
#					|		|		|	|	|		index = Int(-1)
#					|		|		|	|	|		selected_item = Property(cached=True)
#					|		|		|	|	|		editable = Bool(False)
#					|		|		|	|	|		hug_width = set_default('weak')
#					|		|		|	|	|		proxy = Typed(ProxyComboBox)
#	widgets			|		|		|	|	+--	DualSlider
#					|		|		|	|	|		minimum = Int(0)
#					|		|		|	|	|		maximum = Int(100)
#					|		|		|	|	|		low_value = Int()
#					|		|		|	|	|		high_value = Int()
#					|		|		|	|	|		tick_position = TickPosition('bottom')
#					|		|		|	|	|		tick_interval = Range(low=0)
#					|		|		|	|	|		orientation = Enum('horizontal', 'vertical')
#					|		|		|	|	|		auto_hug = Bool(True)
#					|		|		|	|	|		proxy = Typed(ProxySeparator)
#	widgets			|		|		|	|	+--	Field
#					|		|		|	|	|	|	<Container
#					|		|		|	|	|	|	>(Menu)
#					|		|		|	|	|	|	text = Str()
#					|		|		|	|	|	|	mask = Str()
#					|		|		|	|	|	|	validator = Typed(Validator)
#					|		|		|	|	|	|	submit_triggers = List(Enum('lost_focus', 'return_pressed', 'auto_sync'), ['lost_focus', 'return_pressed'])
#					|		|		|	|	|	|	sync_time = Int(300)
#					|		|		|	|	|	|	placeholder = Str()
#					|		|		|	|	|	|	echo_mode = Enum('normal', 'password', 'silent')
#					|		|		|	|	|	|	max_length = Int(0)
#					|		|		|	|	|	|	read_only = Bool(False)
#					|		|		|	|	|	|	text_align = Enum('left', 'right', 'center')
#					|		|		|	|	|	|	hug_width = set_default('ignore')
#					|		|		|	|	|	|	proxy = Typed(ProxyField)
#					|		|		|	|	|	|	#
#					|		|		|	|	|	|	self.field_text()
#	(stdlib)		|		|		|	|	|	+--	FloatField
#	(stdlib)		|		|		|	|	|	+--	IntField
#	(stdlib)		|		|		|	|	|	+--	RegexField
#	(enamlx)		|		|		|	|	+--	GraphicsView
#	(enamlx)		|		|		|	|	|		>GraphicsItem
#	widgets			|		|		|	|	+--	Html
#					|		|		|	|	|		<Container
#					|		|		|	|	|		:WebView
#					|		|		|	|	|		source = Str()
#					|		|		|	|	|		hug_width = set_default('ignore')
#					|		|		|	|	|		hug_height = set_default('ignore')
#					|		|		|	|	|		proxy = Typed(ProxyHtml)
#	widgets			|		|		|	|	+--	ImageView
#					|		|		|	|	|		<Container
#					|		|		|	|	|		image = Typed(Image)
#					|		|		|	|	|		scale_to_fit = Bool(False)
#					|		|		|	|	|		allow_upscaling = Bool(True)
#					|		|		|	|	|		preserve_aspect_ratio = Bool(True)
#					|		|		|	|	|		hug_width = set_default('weak')
#					|		|		|	|	|		hug_height = set_default('weak')
#					|		|		|	|	|		proxy = Typed(ProxyImageView)
#					|		|		|	|	|		#
#					|		|		|	|	|		layout_constraints => ():
#	widgets	*		|		|		|	|	+--	IPythonConsole
#					|		|		|	|	|		<Container
#					|		|		|	|	|		initial_ns = Dict()
#					|		|		|	|	|		exit_requested :: Event()
#					|		|		|	|	|		hug_width = set_default('ignore')
#					|		|		|	|	|		hug_height = set_default('ignore')
#					|		|		|	|	|		proxy = Typed(ProxyIPythonConsole)
#					|		|		|	|	|		#
#					|		|		|	|	|		self.get_var(name, default=None)
#					|		|		|	|	|		self.update_ns(**kwargs)
#	(enamlx)		|		|		|	|	+--	KeyEvent
#	widgets			|		|		|	|	+--	Label
#					|		|		|	|	|		<Container
#					|		|		|	|	|		text = Str()
#					|		|		|	|	|		align = Enum('left', 'right', 'center', 'justify')
#					|		|		|	|	|		vertical_align = Enum('center', 'top', 'bottom')
#					|		|		|	|	|		link_activated :: Event()
#					|		|		|	|	|		hug_width = set_default('weak')
#					|		|		|	|	|		proxy = Typed(ProxyLabel)
#	widgets			|		|		|	|	+--	MPLCanvas
#					|		|		|	|	|		<Container
#					|		|		|	|	|		figure = ForwardTyped(Figure)
#					|		|		|	|	|		toolbar_visible = Bool(False)
#					|		|		|	|	|		hug_width = set_default('ignore')
#					|		|		|	|	|		hug_height = set_default('ignore')
#					|		|		|	|	|		proxy = Typed(ProxyMPLCanvas)
#	widgets			|		|		|	|	+--	MultilineField
#					|		|		|	|	|		<Container
#					|		|		|	|	|		text = Str()
#					|		|		|	|	|		read_only = Bool(False)
#					|		|		|	|	|		auto_sync_text = Bool(True)
#					|		|		|	|	|		hug_width = set_default('ignore')
#					|		|		|	|	|		hug_height = set_default('ignore')
#					|		|		|	|	|		proxy = Typed(ProxyMultilineField)
#					|		|		|	|	|		#
#					|		|		|	|	|		self.sync_text()
#					|		|		|	|	|		self.field_text()
#	widgets			|		|		|	|	+--	ObjectCombo
#					|		|		|	|	|		<Container
#					|		|		|	|	|		:ComboBox
#					|		|		|	|	|		items = List()
#					|		|		|	|	|		selected = Str()
#					|		|		|	|	|		to_string = Callable(str)
#					|		|		|	|	|		to_icon = Callable(lambda item: None)
#					|		|		|	|	|		editable = Bool(False)
#					|		|		|	|	|		hug_width = set_default('weak')
#					|		|		|	|	|		proxy = Typed(ProxyObjectCombo)
#	(enamlx)		|		|		|	|	+--	OccViewer
#	(enamlx)		|		|		|	|	+--	PlotItem
#	(enamlx)		|		|		|	|	|	+--	PlotItem2D
#	(enamlx)		|		|		|	|	|	|	+--	PlotItem3D
#	(enamlx)		|		|		|	|	|	|	|	+--	PlotItemArray3D
#	(enamlx)		|		|		|	|	|	|	+--	PlotItemArray
#	(enamlx)		|		|		|	|	|	+--	AbstractDataPlotItem
#	(enamlx)		|		|		|	|	|		+--	PlotItemDict
#	(enamlx)		|		|		|	|	|		+--	PlotItemList
#	widgets			|		|		|	|	+--	ProgressBar
#					|		|		|	|	|		<Container
#					|		|		|	|	|		minimum = Int(0)
#					|		|		|	|	|		maximum = Int(100)
#					|		|		|	|	|		value = Int(0)
#					|		|		|	|	|		percentage = Property(cached=True)
#					|		|		|	|	|		text_visible = Bool(False)
#					|		|		|	|	|		hug_width = set_default('ignore')
#					|		|		|	|	|		proxy = Typed(ProxyProgressBar)
#					|		|		|	|	|		#
#					|		|		|	|	|		self.get_percentage()
#	widgets			|		|		|	|	+--	RawWidget
#					|		|		|	|	|		proxy = Typed(ProxyRawWidget)
#					|		|		|	|	|		#
#					|		|		|	|	|		self.create_widget(parent)
#					|		|		|	|	|		self.get_widget()
#	scintilla		|		|		|	|	+--	Scintilla
#					|		|		|	|	|		<Container
#					|		|		|	|	|		>ScintillaDocument
#					|		|		|	|	|		>(ScintillaIndicator)
#					|		|		|	|	|		>(ScintillaMarker)
#					|		|		|	|	|		autocomplete = Enum('none', 'all', 'document', 'apis')
#					|		|		|	|	|		autocompletions = List(str)
#					|		|		|	|	|		cursor_position = Tuple()
#					|		|		|	|	|		document = Typed(ScintillaDocument, ())
#					|		|		|	|	|		syntax = Enum(*SYNTAXES)
#					|		|		|	|	|		theme = Typed(dict, ())
#					|		|		|	|	|		settings = Typed(dict, ())
#					|		|		|	|	|		zoom = Int()
#					|		|		|	|	|		text_changed :: Event()
#					|		|		|	|	|		hug_width = set_default('ignore')
#					|		|		|	|	|		hug_height = set_default('ignore')
#					|		|		|	|	|		markers = List(ScintillaMarker)
#					|		|		|	|	|		indicators = List(ScintillaIndicator)
#					|		|		|	|	|		proxy = Typed(ProxyScintilla)
#					|		|		|	|	|		#
#					|		|		|	|	|		self.get_text()
#					|		|		|	|	|		self.set_text(text)
#	widgets			|		|		|	|	+--	Separator
#					|		|		|	|	|		<Container
#					|		|		|	|	|		orientation = Enum('horizontal', 'vertical')
#					|		|		|	|	|		line_style = Enum('sunken', 'raised', 'plain')
#					|		|		|	|	|		line_width = Range(low=0, high=3, value=1)
#					|		|		|	|	|		midline_width = Range(low=0, high=3, value=0)
#					|		|		|	|	|		auto_hug = Bool(True)
#					|		|		|	|	|		proxy = Typed(ProxySeparator)
#	widgets			|		|		|	|	+--	Slider
#					|		|		|	|	|		<Container
#					|		|		|	|	|		>(SliderTransform)
#					|		|		|	|	|		>(FloatTransform)
#					|		|		|	|	|		minimum = Int(0)
#					|		|		|	|	|		maximum = Int(100)
#					|		|		|	|	|		value = Int(0)
#					|		|		|	|	|		single_step = Range(low=1)
#					|		|		|	|	|		page_step = Range(low=1, value=10)
#					|		|		|	|	|		tick_position = TickPosition('bottom')
#					|		|		|	|	|		tick_interval = Range(low=0)
#					|		|		|	|	|		orientation = Enum('horizontal', 'vertical')
#					|		|		|	|	|		tracking = Bool(True)
#					|		|		|	|	|		auto_hug = Bool(True)
#					|		|		|	|	|		proxy = Typed(ProxySlider)
#	widgets			|		|		|	|	+--	SpinBox
#					|		|		|	|	|	|	<Container
#					|		|		|	|	|	|	minimum = Int(0)
#					|		|		|	|	|	|	maximum = Int(100)
#					|		|		|	|	|	|	value = Int(0)
#					|		|		|	|	|	|	prefix = Str()
#					|		|		|	|	|	|	suffix = Str()
#					|		|		|	|	|	|	special_value_text = Str()
#					|		|		|	|	|	|	single_step = Range(low=1)
#					|		|		|	|	|	|	read_only = Bool(False)
#					|		|		|	|	|	|	wrapping = Bool(False)
#					|		|		|	|	|	|	hug_width = set_default('ignore')
#					|		|		|	|	|	|	proxy = Typed(ProxySpinBox)
#	(enamlx)		|		|		|	|	|	+--	DoubleSpinBox
#	widgets			|		|		|	|	+--	VTKCanvas
#					|		|		|	|	|		<Container
#					|		|		|	|	|		renderer = vtkRenderer
#					|		|		|	|	|		renderers = List(vtkRenderer)
#					|		|		|	|	|		hug_width = set_default('ignore')
#					|		|		|	|	|		hug_height = set_default('ignore')
#					|		|		|	|	|		proxy = Typed(ProxyVTKCanvas)
#					|		|		|	|	|		#
#					|		|		|	|	|		self.render()
#	widgets			|		|		|	|	+--	WebView
#					|		|		|	|			<Container
#					|		|		|	|			:Html
#					|		|		|	|			url = Str()
#					|		|		|	|			html = Str()
#					|		|		|	|			base_url = Str()
#					|		|		|	|			hug_width = set_default('ignore')
#					|		|		|	|			hug_height = set_default('ignore')
#					|		|		|	|			proxy = Typed(ProxyWebView)
#	widgets			|		|		|	+--	DockArea
#					|		|		|	|		<Container
#					|		|		|	|		>DockItem
#					|		|		|	|		layout = Coerced(DockLayout, ())
#					|		|		|	|		tab_position = Enum('top', 'bottom', 'left', 'right')
#					|		|		|	|		live_drag = Bool(True)
#					|		|		|	|		style = Str('vs-2010')
#					|		|		|	|		dock_events_enabled = Bool(False)
#					|		|		|	|		dock_event :: Event(DockEvent)
#					|		|		|	|		hug_width = set_default('ignore')
#					|		|		|	|		hug_height = set_default('ignore')
#					|		|		|	|		proxy = Typed(ProxyDockArea)
#					|		|		|	|		#
#					|		|		|	|		self.initialized()
#					|		|		|	|		self.dock_items()
#					|		|		|	|		self.save_layout()
#					|		|		|	|		self.apply_layout(layout)
#					|		|		|	|		self.update_layout(ops)
#					|		|		|	|		self.suppress_dock_events(ops)
#					|		|		|	+--	Frame
#					|		|		|	|	|	border = Typed(Border)
#					|		|		|	|	|	proxy = Typed(ProxyFrame)
#	widgets			|		|		|	|	+--	Container
#					|		|		|	|	|	|	>ConstraintsWidget
#					|		|		|	|	|	|	share_layout = Bool(False)
#					|		|		|	|	|	|	padding = Coerced(Box, (10, 10, 10, 10))
#					|		|		|	|	|	|	resist_width = set_default('ignore')
#					|		|		|	|	|	|	resist_height = set_default('ignore')
#					|		|		|	|	|	|	hug_width = set_default('ignore')
#					|		|		|	|	|	|	hug_height = set_default('ignore')
#					|		|		|	|	|	|	proxy = Typed(ProxyContainer)
#					|		|		|	|	|	|	#
#					|		|		|	|	|	|	self.widgets()
#					|		|		|	|	|	|	self.visible_widgets()
#					|		|		|	|	|	|	self.child_added(child)
#					|		|		|	|	|	|	self.child_moved(child)
#					|		|		|	|	|	|	self.child_removed(child)
#					|		|		|	|	|	|	self.layout_constraints(child)
#	(enamlx)		|		|		|	|	|	+--	Console
#	(stdlib)		|		|		|	|	|	+--	DialogButtonBox
#	widgets			|		|		|	|	|	+--	GroupBox
#					|		|		|	|	|	|		>WIDGETS
#					|		|		|	|	|	|		title = Str()
#					|		|		|	|	|	|		flat = Bool(False)
#					|		|		|	|	|	|		title_align = Enum('left', 'right', 'center')
#					|		|		|	|	|	|		proxy = Typed(ProxyGroupBox)
#	widgets			|		|		|	|	|	+--	Form
#					|		|		|	|	|	|		>WIDGETS
#					|		|		|	|	|	|		midline = ConstraintMember()
#					|		|		|	|	|	|		row_spacing = Int(10)
#					|		|		|	|	|	|		column_spacing = Int(10)
#					|		|		|	|	|	|		#
#					|		|		|	|	|	|		layout_constraints => ():
#	widgets			|		|		|	|	|	+--	HGroup
#					|		|		|	|	|	|		>WIDGETS
#					|		|		|	|	|	|		spacing = Int(10)
#					|		|		|	|	|	|		leading_spacer = Typed(Spacer)
#					|		|		|	|	|	|		trailing_spacer = Typed(Spacer)
#					|		|		|	|	|	|		align_widths = Bool(True)
#					|		|		|	|	|	|		#
#					|		|		|	|	|	|		layout_constraints => ():
#	(enamlx)		|		|		|	|	|	+--	PlotArea
#	(stdlib)		|		|		|	|	|	+--	TaskDialogBody
#					|		|		|	|	|	|		>WIDGETS
#					|		|		|	|	|	|		padding = 0
#					|		|		|	|	|	|		Separator
#					|		|		|	|	|	|		#
#					|		|		|	|	|	|		layout_constraints => ():
#	(stdlib)		|		|		|	|	|	+--	TaskDialogCommandArea
#					|		|		|	|	|	|		>WIDGETS
#	(stdlib)		|		|		|	|	|	+--	TaskDialogContentArea
#					|		|		|	|	|	|		>WIDGETS
#					|		|		|	|	|	|		padding = (0, 10, 15, 10)
#	(stdlib)		|		|		|	|	|	+--	TaskDialogDetailsArea
#					|		|		|	|	|	|		>WIDGETS
#					|		|		|	|	|	|		padding = (0, 10, 15, 10)
#					|		|		|	|	|	|		visible :: parent.request_relayout()
#	(stdlib)		|		|		|	|	|	+--	TaskDialogFootnoteArea
#					|		|		|	|	|	|		>WIDGETS
#	(stdlib)		|		|		|	|	|	+--	TaskDialogIconArea
#					|		|		|	|	|	|		>WIDGETS
#					|		|		|	|	|	|		padding = (10, 0, 15, 10)
#					|		|		|	|	|	|		resist_height = 'strong'
#					|		|		|	|	|	|		#
#					|		|		|	|	|	|		layout_constraints => ():
#	(stdlib)		|		|		|	|	|	+--	TaskDialogInstructionArea
#					|		|		|	|	|	|		>WIDGETS
#					|		|		|	|	|	|		padding = (10, 10, 15, 10)
#	widgets			|		|		|	|	|	+--	VGroup
#					|		|		|	|	|			>WIDGETS
#					|		|		|	|	|			>(Container)
#					|		|		|	|	|			spacing = Int(10)
#					|		|		|	|	|			leading_spacer = Typed(Spacer)
#					|		|		|	|	|			trailing_spacer = Typed(Spacer)
#					|		|		|	|	|			#
#					|		|		|	|	|			layout_constraints => ():
#	widgets			|		|		|	|	+--	FlowArea
#					|		|		|	|	|		<Container
#					|		|		|	|	|		>FlowItem
#					|		|		|	|	|		>(Include)
#					|		|		|	|	|		direction = Enum('left_to_right', 'right_to_left', 'top_to_bottom', 'bottom_to_top')
#					|		|		|	|	|		align = Enum('leading', 'trailing', 'center', 'justify')
#					|		|		|	|	|		horizontal_spacing = Range(low=0, value=10)
#					|		|		|	|	|		vertical_spacing = Range(low=0, value=10)
#					|		|		|	|	|		margins = Coerced(Box, (10, 10, 10, 10))
#					|		|		|	|	|		hug_width = set_default('ignore')
#					|		|		|	|	|		hug_height = set_default('ignore')
#					|		|		|	|	|		proxy = Typed(ProxyFlowArea)
#					|		|		|	|	|		#
#					|		|		|	|	|		self.flow_items()
#	widgets			|		|		|	|	+--	ScrollArea
#					|		|		|	|			<Container
#					|		|		|	|			>Container
#					|		|		|	|			horizontal_policy = Enum('as_needed', 'always_on', 'always_off')
#					|		|		|	|			vertical_policy = Enum('as_needed', 'always_on', 'always_off')
#					|		|		|	|			widget_resizable = Bool(True)
#					|		|		|	|			hug_width = set_default('ignore')
#					|		|		|	|			hug_height = set_default('ignore')
#					|		|		|	|			proxy = Typed(ProxyScrollArea)
#					|		|		|	|			#
#					|		|		|	|			self.scroll_widget()
#	widgets			|		|		|	+--	MdiArea
#					|		|		|	|		<Container
#					|		|		|	|		>MdiWindow
#					|		|		|	|		>(Include)
#					|		|		|	|		hug_width = set_default('ignore')
#					|		|		|	|		hug_height = set_default('ignore')
#					|		|		|	|		resist_width = set_default('weak')
#					|		|		|	|		resist_height = set_default('weak')
#					|		|		|	|		proxy = Typed(ProxyMdiArea)
#					|		|		|	|		#
#					|		|		|	|		self.mdi_windows()
#					|		|		|	|		self.tile_mdi_windows()
#					|		|		|	|		self.cascade_mdi_windows()
#					|		|		|	|		self.child_added(child)
#	widgets			|		|		|	+--	Notebook
#					|		|		|	|		<Container
#					|		|		|	|		>Page
#					|		|		|	|		>(Include)
#					|		|		|	|		:Stack
#					|		|		|	|		tab_style = Enum('document', 'preferences')
#					|		|		|	|		tab_position = Enum('top', 'bottom', 'left', 'right')
#					|		|		|	|		tabs_closable = Bool(True)
#					|		|		|	|		tabs_movable = Bool(True)
#					|		|		|	|		selected_tab = Str()
#					|		|		|	|		size_hint_mode = Enum('union', 'current')
#					|		|		|	|		hug_width = set_default('ignore')
#					|		|		|	|		hug_height = set_default('ignore')
#					|		|		|	|		proxy = Typed(ProxyNotebook)
#					|		|		|	|		#
#					|		|		|	|		self.pages()
#	widgets			|		|		|	+--	Splitter
#					|		|		|	|		<Container
#					|		|		|	|		>SplitItem
#					|		|		|	|		orientation = Enum('horizontal', 'vertical')
#					|		|		|	|		live_drag = Bool(True)
#					|		|		|	|		hug_width = set_default('ignore')
#					|		|		|	|		hug_height = set_default('ignore')
#					|		|		|	|		proxy = Typed(ProxySplitter)
#					|		|		|	|		#
#					|		|		|	|		self.split_items()
#	widgets			|		|		|	+--	Stack
#					|		|		|	|		>StackItem
#					|		|		|	|		:Notebook
#					|		|		|	|		index = Int(0)
#					|		|		|	|		transition = Typed(Transition)
#					|		|		|	|		size_hint_mode = Enum('union', 'current')
#					|		|		|	|		hug_width = set_default('ignore')
#					|		|		|	|		hug_height = set_default('ignore')
#					|		|		|	|		proxy = Typed(ProxyStack)
#					|		|		|	|		#
#					|		|		|	|		self.stack_items()
#	widgets			|		|		|	+--	ToolBar
#					|		|		|			<MainWindow
#					|		|		|			<(Container)
#					|		|		|			>Action
#					|		|		|			>ActionGroup
#					|		|		|			>ToolButton
#					|		|		|			button_style = Enum('icon_only', 'text_only', 'text_beside_icon', 'text_under_icon')
#					|		|		|			movable = Bool(True)
#					|		|		|			floatable = Bool(True)
#					|		|		|			floating = Bool(False)
#					|		|		|			dock_area = Enum('top', 'right', 'left', 'bottom')
#					|		|		|			allowed_dock_areas = List(Enum('top', 'right', 'left', 'bottom', 'all'), ['all'],)
#					|		|		|			orientation = Enum('horizontal', 'vertical')
#					|		|		|			auto_hug :: Event()
#					|		|		|			proxy = Typed(ProxyToolBar)
#					|		|		|			#
#					|		|		|			self.items()
#	widgets			|		|		+--	DockItem
#					|		|		|		<DockArea
#					|		|		|		>Container
#					|		|		|		title = Str()
#					|		|		|		title_editable = Bool(False)
#					|		|		|		title_bar_visible = Bool(True)
#					|		|		|		icon = Typed(Icon)
#					|		|		|		icon_size = Coerced(Size, (-1, -1))
#					|		|		|		stretch = Range(low=0, value=1)
#					|		|		|		closable = Bool(True)
#					|		|		|		title_bar_right_clicked :: Event()
#					|		|		|		closing :: Event(CloseEvent)
#					|		|		|		closed :: Event()
#					|		|		|		proxy = Typed(ProxyDockItem)
#					|		|		|		#
#					|		|		|		self.dock_widget()
#					|		|		|		self.alert(level, on=250, off=250, repeat=4, persist=False)
#	widgets			|		|		+--	DockPane
#					|		|		|		<MainWindow
#					|		|		|		>Container
#					|		|		|		title = Str()
#					|		|		|		title_bar_visible = Bool(True)
#					|		|		|		title_bar_orientation = num('horizontal', 'vertical')
#					|		|		|		closable = Bool(True)
#					|		|		|		movable = Bool(True)
#					|		|		|		floatable = Bool(True)
#					|		|		|		floating = Bool(False)
#					|		|		|		dock_area = Enum('left', 'right', 'top', 'bottom')
#					|		|		|		allowed_dock_areas = List(Enum('left', 'right', 'top', 'bottom', 'all'), ['all'],)
#					|		|		|		closed :: Event()
#					|		|		|		proxy = Typed(ProxyDockPane)
#					|		|		|		#
#					|		|		|		self.dock_widget()
#	widgets			|		|		+--	FlowItem
#					|		|		|		<FlowArea
#					|		|		|		>Container
#					|		|		|		preferred_size = Bool(True)
#					|		|		|		align = Enum('leading', 'trailing', 'center')
#					|		|		|		stretch = Range(low=0, value=0)
#					|		|		|		ortho_stretch = Range(low=0, value=0)
#					|		|		|		proxy = Typed(ProxyFlowItem)
#					|		|		|		#
#					|		|		|		self.flow_widget()
#	widgets			|		|		+--	MdiWindow
#					|		|		|		<MdiArea
#					|		|		|		>Container
#					|		|		|		title = Str()
#					|		|		|		icon = Typed(Icon)
#					|		|		|		#
#					|		|		|		self.mdi_widget()
#	widgets			|		|		+--	Page
#					|		|		|		<Notebook
#					|		|		|		>Container
#					|		|		|		title = Str()
#					|		|		|		icon = Typed(Icon)
#					|		|		|		closable = Bool(True)
#					|		|		|		closed :: Event()
#					|		|		|		proxy = Typed(ProxyPage)
#					|		|		|		#
#					|		|		|		self.page_widget()
#	widgets			|		|		+--	PopupView
#					|		|		|		<Window
#					|		|		|		<Widget
#					|		|		|		>Container
#					|		|		|		popup_views = List()
#					|		|		|		window_type = Enum('popup', 'tool_tip', 'window')
#					|		|		|		anchor_mode = Enum('parent', 'cursor')
#					|		|		|		parent_anchor = Coerced(PosF, (0.5, 0.5), coercer=coerce_posf)
#					|		|		|		anchor = Coerced(PosF, (0.5, 0.0), coercer=coerce_posf)
#					|		|		|		offset = Coerced(Pos, (0, 0), coercer=coerce_pos)
#					|		|		|		arrow_edge = Enum('top', 'bottom', 'left', 'right')
#					|		|		|		arrow_size = Int(0)
#					|		|		|		timeout = Float(0.0)
#					|		|		|		fade_in_duration = Int(100)
#					|		|		|		fade_out_duration = Int(100)
#					|		|		|		close_on_click = Bool(True)
#					|		|		|		translucent_background = Bool(True)
#					|		|		|		closed :: Event()
#					|		|		|		visible = set_default(False)
#					|		|		|		proxy = Typed(ProxyPopupView)
#					|		|		|		#
#					|		|		|		self.central_widget()
#					|		|		|		self.show()
#					|		|		|		self.close()
#	widgets			|		|		+--	SplitItem
#					|		|		|		<Splitter
#					|		|		|		>Container
#					|		|		|		stretch = Range(low=0, value=1)
#					|		|		|		collapsible = Bool(True)
#					|		|		|		proxy = Typed(ProxySplitItem)
#					|		|		|		#
#					|		|		|		self.split_widget()
#	widgets			|		|		+--	StackItem
#					|		|		|		<Stack
#					|		|		|		proxy = Typed(ProxyStackItem)
#					|		|		|		#
#					|		|		|		self.stack_widget()
#	widgets			|		|		+--	StatusBar
#					|		|		|		<MainWindow
#					|		|		|		>StatusItem
#					|		|		|		size_grip_enabled = Bool(True)
#					|		|		|		proxy = Typed(ProxyStatusBar)
#					|		|		|		#
#					|		|		|		self.status_items()
#					|		|		|		self.show_message(message, timeout=0)
#					|		|		|		self.clear_message()
#	widgets			|		|		+--	Window
#					|		|			|	windows = set()
#					|		|			|	title = Str()
#					|		|			|	initial_position = Coerced(Pos, (-1, -1))
#					|		|			|	initial_size = Coerced(Size, (-1, -1))
#					|		|			|	modality = Enum('non_modal', 'application_modal', 'window_modal')
#					|		|			|	destroy_on_close = Bool(True)
#					|		|			|	icon = Typed(Icon)
#					|		|			|	always_on_top = Bool(False)
#					|		|			|	closing :: Event(CloseEvent)
#					|		|			|	closed :: Event()
#					|		|			|	visible = set_default(False)
#					|		|			|	proxy = Typed(ProxyWindow)
#					|		|			|	#
#					|		|			|	self.initialize()
#					|		|			|	self.destroy()
#					|		|			|	self.central_widget()
#					|		|			|	self.position()
#					|		|			|	self.set_position(pos)
#					|		|			|	self.size()
#					|		|			|	self.set_size(size)
#					|		|			|	self.geometry()
#					|		|			|	self.set_geometry(rect)
#					|		|			|	self.frame_geometry()
#					|		|			|	self.maximize()
#					|		|			|	self.is_maximized()
#					|		|			|	self.minimize()
#					|		|			|	self.is_minimized()
#					|		|			|	self.restore()
#					|		|			|	self.send_to_front()
#					|		|			|	self.send_to_back()
#					|		|			|	self.activate_window()
#					|		|			|	self.center_on_screen()
#					|		|			|	self.center_on_widget(other)
#					|		|			|	self.close()
#					|		|			|	self.show()
#	widgets			|		|			+--	Dialog
#					|		|			|	|	result = Bool(False)
#					|		|			|	|	finished :: Event(bool)
#					|		|			|	|	accepted :: Event()
#					|		|			|	|	rejected :: Event()
#					|		|			|	|	modality = set_default('application_modal')
#					|		|			|	|	proxy = Typed(ProxyDialog)
#					|		|			|	|	#
#					|		|			|	|	self.exec_()
#					|		|			|	|	self.done(result)
#					|		|			|	|	self.accept()
#					|		|			|	|	self.reject()
#	(stdlib)		|		|			|	+--	MessageBox
#	widgets			|		|			+--	MainWindow
#					|		|				|	<(Enaml)
#					|		|				|	>DockPane
#					|		|				|	>MenuBar
#					|		|				|	>StatusBar
#					|		|				|	>ToolBar
#					|		|				|	proxy = Typed(ProxyMainWindow)
#					|		|				|	#
#					|		|				|	self.menu_bar()
#					|		|				|	self.dock_panes()
#					|		|				|	self.status_bar()
#					|		|				|	self.tool_bars()
#					|		|				+--	WorkbenchWindow
#	workbench.ui	|		+--	Workspace
#					|				window_title = Str()
#					|				content = Typed(Container)
#					|				workbench = Typed(Workbench)
#					|				#
#					|				self.start()
#					|				self.stop()
#					+--	PathNode
#					|	|	self.path = Str()
#					|	|	self.parent_path = Str()
#					|	|	self.id = Str()
#					|	|	#
#					|	|	self.assemble()
#					|	+--	ActionNode
#					|	|		workbench = Typed(Workbench)
#					|	|		#
#					|	|		self.assemble()
#					|	+--	MenuNode
#					|		|	children = List(PathNode)
#					|		|	#
#					|		|	self.group_data()
#					|		|	self.collect_child_groups()
#					|		|	self.create_children()
#					|		|	self.assemble_children()
#					|		|	self.assemble()
#					|		+--	RootMenuNode
#					|				self.group_data()
#					|				self.assemble()
#	(enamlx)		+--	Pen
#	workbench		+--	Plugin
#					|	|	self.workbench
#					|	|	#
#					|	|	self.start()
#					|	|	self.stop()
#					|	+--	UIPlugin
#					|			self.window
#					|			self.workspace
#					|			#
#					|			self.start()
#					|			self.stop()
#					|			self.show_window()
#					|			self.hide_window()
#					|			self.start_application()
#					|			self.stop_application()
#					|			self.close_window()
#					|			self.close_workspace()
#					|			self.select_workspace(extension_id)
#	(enamlx)		+--	Point
#	(enamlx)		+--	Rect
#	scintilla		+--	ScintillaDocument
#					|		<Scintilla
#					|		uuid = Constant()
#	scintilla		+--	ScintillaIndicator
#					|		<Scintilla
#					|		start = Tuple()
#					|		stop = Tuple()
#					|		style = Enum('squiggle', 'plain', 'tt', 'diagonal', 'strike', 'hidden', 'box', 'round_box', 'straight_box', 'full_box', 'dashes', 'dots', 'squiggle_low', 'dot_box', 'thick_composition', 'thin_composition', 'text_color', 'triangle', 'triangle_character')
#					|		color = Str("#000000")
#	scintilla		+--	ScintillaMarker
#					|		<Scintilla
#					|		line = Int()
#					|		image = Typed(Image)
#					+--	Spacer
#					|	|	size = Range(low=0)
#					|	|	strength = StrengthMember()
#					|	|	#
#					|	|	self.__init__(size, strength=None)
#					|	|	self.__or__(strength)
#					|	|	self.when(switch)
#					|	|	self.create_constraints(first, second)
#					|	|	#
#					|	|	constraints => (first, second):
#					|	+--	EqSpacer
#					|	|		self.constraints(first, second)
#					|	+--	FlexSpacer
#					|	|		min_strength = StrengthMember(kiwi.strength.required)
#					|	|		eq_strength = StrengthMember(kiwi.strength.medium * 1.25)
#					|	|		#
#					|	|		self.__init__(size, min_strength=None, eq_strength=None)
#					|	|		self.constraints(first, second)
#					|	+--	GeSpacer
#					|	|		self.constraints(first, second)
#					|	+--	LayoutSpacer
#					|	|		self.__call__(*args, **kwargs)
#					|	|		self.__or__(strength)
#					|	|		self.__eq__(size)
#					|	|		self.__le__(size)
#					|	|		self.__ge__(size)
#					|	|		self.flex(**kwargs)
#					|	|		self.constraints(first, second)
#					|	+--	LeSpacer
#					|			self.constraints(first, second)
#	widgets			+--	Transition
#					|		type = Enum('slide', 'wipe', 'iris', 'fade', 'crossfade')
#					|		direction = Enum('left_to_right', 'right_to_left', 'top_to_bottom', 'bottom_to_top')
#					|		duration = Range(low=0, value=250)
#					+--	Validator
#					|	|	message = Str()
#					|	|	#
#					|	|	self.validate(text)
#					|	|	self.fixup(text)
#					|	+--	FloatValidator
#					|	|		minimum = Typed(float)
#					|	|		maximum = Typed(float)
#					|	|		allow_exponent = Bool(True)
#					|	|		#
#					|	|		self.validate(text)
#					|	+--	IntValidator
#					|	|		minimum = Typed(int)
#					|	|		maximum = Typed(int)
#					|	|		base = Enum(10, 2, 8, 16)
#					|	|		#
#					|	|		self.validate(text)
#					|	+--	RegexValidator
#					|			regex = Str(r'.*')
#					|			#
#					|			self.validate(text)
#					+--	WindowModel
#					|		branding = Typed(Branding, ())
#					|		menus = List(Menu)
#					|		workspace = Typed(Workspace, ())
#	workbench		+--	Workbench
#						|	plugin_added :: Event(str)
#						|	plugin_removed :: Event(str)
#						|	extension_point_added :: Event(str)
#						|	extension_point_removed :: Event(str)
#						|	#
#						|	self.register(manifest)
#						|	self.unregister(plugin_id)
#						|	self.get_manifest(plugin_id)
#						|	self.get_plugin(plugin_id, force_create=True)
#						|	self.get_extension_point(extension_point_id)
#						|	self.get_extension_points(self)
#	workbench.ui		+--	UIWorkbench
#								self.run()

#	(atom)			(Coerced)
#					+--	ColorMember
#					+--	FontMember

#	(atom)			(Value)
#					+--	StrengthMember
#							self.__init__(default=None, factory=None)
#							self.validate(owner, old, new)

#	(atom)			(IntEnum)
#	widgets			+--	Feature

#					(tuple)
#					+--	BaseBox
#					|	|	top = int
#					|	|	right = int
#					|	|	bottom = int
#					|	|	left = int
#					|	|	#
#					|	|	cls.coerce_type(item)
#					|	|	#
#					|	|	self.__new__(top=None, right=None, bottom=None, left=None)
#					|	|	self.__getnewargs__()
#					|	|	self.__repr__()
#	layout			|	+--	Box
#					|	|		rect = Rect()
#					|	|		size = Size()
#					|	|		pos = Pos()
#					|	|		#
#					|	|		cls.coerce_type(item)
#	layout			|	+--	BoxF
#					|			top = float
#					|			right = float
#					|			bottom = float
#					|			left = float
#					|			rect = RectF()
#					|			size = SizeF()
#					|			pos = PosF()
#					|			#
#					|			cls.coerce_type(item)
#					+--	BasePos
#					|	|	x = int
#					|	|	y = int
#					|	|	#
#					|	|	cls.coerce_type(item)
#					|	|	#
#					|	|	self.__new__(x=None, y=None)
#					|	|	self.__getnewargs__()
#					|	|	self.__repr__()
#	layout			|	+--	Pos
#					|	|		cls.coerce_type(item)
#	layout			|	+--	PosF
#					|			x = float
#					|			y = float
#					|			#
#					|			cls.coerce_type(item)
#					+--	BaseRect
#					|	|	x = int
#					|	|	y = int
#					|	|	width = int
#					|	|	height = int
#					|	|	#
#					|	|	cls.coerce_type(item)
#					|	|	#
#					|	|	self.__new__(x=None, y=None, width=None, height=None)
#					|	|	self.__getnewargs__()
#					|	|	self.__repr__()
#	layout			|	+--	Rect
#					|	|		box = Box()
#					|	|		pos = Pos()
#					|	|		size = Size()
#					|	|		#
#					|	|		cls.coerce_type(item)
#	layout			|	+--	RectF
#					|			x = float
#					|			y = float
#					|			width = float
#					|			height = float
#					|			box = BoxF()
#					|			pos = PosF()
#					|			size = SizeF()
#					|			#
#					|			cls.coerce_type(item)
#					+--	BaseSize
#						|	width = int
#						|	height = int
#						|	#
#						|	cls.coerce_type(item)
#						|	#
#						|	self.__new__(width=None, height=None)
#						|	self.__getnewargs__()
#						|	self.__repr__()
#	layout				+--	Size
#						|		cls.coerce_type(item)
#	layout				+--	SizeF
#								width = float
#								height = float
#								#
#								cls.coerce_type(item)

# Syntax sugar (beware, allows lazy/late declaration)

#enamldef NewWidget(BaseWidget):
#template NewWidget(BaseWidget):

#		alias new_name(: specific_thing)
#		attr new_attr(: type = value)
#		const new_const = expr
#		event new_event
#		func new_func(params):

#		a = b : a copy b (static only, no tracking)
#		a := b : a delegate b (mirror value)
#		a << b : a subscribe b (value, expr)
#		a >> b : a update b (value)
#		a :: b : a runs b (expr, minus 'def', 'class', 'lambda', 'return', 'yield')

#		hug_ : deformation
#		resist_ : compression
#		limit_ : expansion
#		weight : 'ignored', 'weak', 'medium', 'strong', 'required'

#		position : BOUNDARY_ATTRS
#		position : .top, .bottom, .left, .right, .v_center, .h_center, .width, .height
#		contents : CONTENT_BOUNDARY_ATTRS
#		contents : contents_top==, contents_right==, contents_bottom==, contents_left==
#		layout : spacer, hbox(), vbox(), horizontal(), vertical(), align(), grid(), factory()
#		horizontal : left, right
#		hbox : spacing=
#		grid : column_align=, row_align=
#		vertical : top, bottom

#		style : 'vs-2010', 'grey-wind', 'new-moon', 'metro'

#		event : change['oldvalue'], change['value'], accept(), ignore()
#		drag : DragData, DropAction, Feature

#		hierarchy : parent.title, parent.children.index(self), ...

# Dependencies and relationship

#	(enaml)
#	+--	BUTTONS
#	|	+--	(Container)
#	|	|	|	constraints = (List())
#	|	|	|	padding =
#	|	|	+--	CheckBox
#	|	|	|		checkable =
#	|	|	|		checked =
#	|	|	|		text =
#	|	|	|		toggled ::
#	|	|	+--	PushButton
#	|	|	|	|	font =
#	|	|	|	|	clicked ::
#	|	|	|	|	constraints =
#	|	|	|	|	enabled <<
#	|	|	|	|	style_class =
#	|	|	|	|	text =
#	|	|	|	+--	(Menu)
#	|	|	|		+--	(Action)
#	|	|	|			text <<
#	|	|	|			triggered ::
#	|	|	+--	RadioButton
#	|	|	|		checkable =
#	|	|	|		text =
#	|	|	+--	ToolButton
#	|	|		|	button_style =
#	|	|		|	icon = Icon(...)
#	|	|		|	popup_mode =
#	|	|		|	text =
#	|	|		+--	(Menu)
#	|	+--	(ToolBar)
#	|		+--	ToolButton
#	+--	COLOR
#	|	+--	(CSS_Color_Name)
#	|			'aliceblue': Color(240, 248, 255)
#	|			'antiquewhite': Color(250, 235, 215)
#	|			'aqua': Color(0, 255, 255)
#	|			'aquamarine': Color(127, 255, 212)
#	|			'azure': Color(240, 255, 255)
#	|			'beige': Color(245, 245, 220)
#	|			'bisque': Color(255, 228, 196)
#	|			'black': Color(0, 0, 0)
#	|			'blanchedalmond': Color(255, 235, 205)
#	|			'blue': Color(0, 0, 255)
#	|			'blueviolet': Color(138, 43, 226)
#	|			'brown': Color(165, 42, 42)
#	|			'burlywood': Color(222, 184, 135)
#	|			'cadetblue': Color(95, 158, 160)
#	|			'chartreuse': Color(127, 255, 0)
#	|			'chocolate': Color(210, 105, 30)
#	|			'coral': Color(255, 127, 80)
#	|			'cornflowerblue': Color(100, 149, 237)
#	|			'cornsilk': Color(255, 248, 220)
#	|			'crimson': Color(220, 20, 60)
#	|			'cyan': Color(0, 255, 255)
#	|			'darkblue': Color(0, 0, 139)
#	|			'darkcyan': Color(0, 139, 139)
#	|			'darkgoldenrod': Color(184, 134, 11)
#	|			'darkgray': Color(169, 169, 169)
#	|			'darkgreen': Color(0, 100, 0)
#	|			'darkgrey': Color(169, 169, 169)
#	|			'darkkhaki': Color(189, 183, 107)
#	|			'darkmagenta': Color(139, 0, 139)
#	|			'darkolivegreen': Color(85, 107, 47)
#	|			'darkorange': Color(255, 140, 0)
#	|			'darkorchid': Color(153, 50, 204)
#	|			'darkred': Color(139, 0, 0)
#	|			'darksalmon': Color(233, 150, 122)
#	|			'darkseagreen': Color(143, 188, 143)
#	|			'darkslateblue': Color(72, 61, 139)
#	|			'darkslategray': Color(47, 79, 79)
#	|			'darkslategrey': Color(47, 79, 79)
#	|			'darkturquoise': Color(0, 206, 209)
#	|			'darkviolet': Color(148, 0, 211)
#	|			'deeppink': Color(255, 20, 147)
#	|			'deepskyblue': Color(0, 191, 255)
#	|			'dimgray': Color(105, 105, 105)
#	|			'dimgrey': Color(105, 105, 105)
#	|			'dodgerblue': Color(30, 144, 255)
#	|			'firebrick': Color(178, 34, 34)
#	|			'floralwhite': Color(255, 250, 240)
#	|			'forestgreen': Color(34, 139, 34)
#	|			'fuchsia': Color(255, 0, 255)
#	|			'gainsboro': Color(220, 220, 220)
#	|			'ghostwhite': Color(248, 248, 255)
#	|			'gold': Color(255, 215, 0)
#	|			'goldenrod': Color(218, 165, 32)
#	|			'gray': Color(128, 128, 128)
#	|			'green': Color(0, 128, 0)
#	|			'greenyellow': Color(173, 255, 47)
#	|			'grey': Color(128, 128, 128)
#	|			'honeydew': Color(240, 255, 240)
#	|			'hotpink': Color(255, 105, 180)
#	|			'indianred': Color(205, 92, 92)
#	|			'indigo': Color(75, 0, 130)
#	|			'ivory': Color(255, 255, 240)
#	|			'khaki': Color(240, 230, 140)
#	|			'lavender': Color(230, 230, 250)
#	|			'lavenderblush': Color(255, 240, 245)
#	|			'lawngreen': Color(124, 252, 0)
#	|			'lemonchiffon': Color(255, 250, 205)
#	|			'lightblue': Color(173, 216, 230)
#	|			'lightcoral': Color(240, 128, 128)
#	|			'lightcyan': Color(224, 255, 255)
#	|			'lightgoldenrodyellow': Color(250, 250, 210)
#	|			'lightgray': Color(211, 211, 211)
#	|			'lightgreen': Color(144, 238, 144)
#	|			'lightgrey': Color(211, 211, 211)
#	|			'lightpink': Color(255, 182, 193)
#	|			'lightsalmon': Color(255, 160, 122)
#	|			'lightseagreen': Color(32, 178, 170)
#	|			'lightskyblue': Color(135, 206, 250)
#	|			'lightslategray': Color(119, 136, 153)
#	|			'lightslategrey': Color(119, 136, 153)
#	|			'lightsteelblue': Color(176, 196, 222)
#	|			'lightyellow': Color(255, 255, 224)
#	|			'lime': Color(0, 255, 0)
#	|			'limegreen': Color(50, 205, 50)
#	|			'linen': Color(250, 240, 230)
#	|			'magenta': Color(255, 0, 255)
#	|			'maroon': Color(128, 0, 0)
#	|			'mediumaquamarine': Color(102, 205, 170)
#	|			'mediumblue': Color(0, 0, 205)
#	|			'mediumorchid': Color(186, 85, 211)
#	|			'mediumpurple': Color(147, 112, 219)
#	|			'mediumseagreen': Color(60, 179, 113)
#	|			'mediumslateblue': Color(123, 104, 238)
#	|			'mediumspringgreen': Color(0, 250, 154)
#	|			'mediumturquoise': Color(72, 209, 204)
#	|			'mediumvioletred': Color(199, 21, 133)
#	|			'midnightblue': Color(25, 25, 112)
#	|			'mintcream': Color(245, 255, 250)
#	|			'mistyrose': Color(255, 228, 225)
#	|			'moccasin': Color(255, 228, 181)
#	|			'navajowhite': Color(255, 222, 173)
#	|			'navy': Color(0, 0, 128)
#	|			'oldlace': Color(253, 245, 230)
#	|			'olive': Color(128, 128, 0)
#	|			'olivedrab': Color(107, 142, 35)
#	|			'orange': Color(255, 165, 0)
#	|			'orangered': Color(255, 69, 0)
#	|			'orchid': Color(218, 112, 214)
#	|			'palegoldenrod': Color(238, 232, 170)
#	|			'palegreen': Color(152, 251, 152)
#	|			'paleturquoise': Color(175, 238, 238)
#	|			'palevioletred': Color(219, 112, 147)
#	|			'papayawhip': Color(255, 239, 213)
#	|			'peachpuff': Color(255, 218, 185)
#	|			'peru': Color(205, 133, 63)
#	|			'pink': Color(255, 192, 203)
#	|			'plum': Color(221, 160, 221)
#	|			'powderblue': Color(176, 224, 230)
#	|			'purple': Color(128, 0, 128)
#	|			'red': Color(255, 0, 0)
#	|			'rosybrown': Color(188, 143, 143)
#	|			'royalblue': Color(65, 105, 225)
#	|			'saddlebrown': Color(139, 69, 19)
#	|			'salmon': Color(250, 128, 114)
#	|			'sandybrown': Color(244, 164, 96)
#	|			'seagreen': Color(46, 139, 87)
#	|			'seashell': Color(255, 245, 238)
#	|			'sienna': Color(160, 82, 45)
#	|			'silver': Color(192, 192, 192)
#	|			'skyblue': Color(135, 206, 235)
#	|			'slateblue': Color(106, 90, 205)
#	|			'slategray': Color(112, 128, 144)
#	|			'slategrey': Color(112, 128, 144)
#	|			'snow': Color(255, 250, 250)
#	|			'springgreen': Color(0, 255, 127)
#	|			'steelblue': Color(70, 130, 180)
#	|			'tan': Color(210, 180, 140)
#	|			'teal': Color(0, 128, 128)
#	|			'thistle': Color(216, 191, 216)
#	|			'tomato': Color(255, 99, 71)
#	|			'turquoise': Color(64, 224, 208)
#	|			'violet': Color(238, 130, 238)
#	|			'wheat': Color(245, 222, 179)
#	|			'white': Color(255, 255, 255)
#	|			'whitesmoke': Color(245, 245, 245)
#	|			'yellow': Color(255, 255, 0)
#	|			'yellowgreen': Color(154, 205, 50)
#	+--	DIALOG
#	|	+--	(Container)
#	|	|	+--	path = FileDialogEx.get_open_file_name(parent=window)
#	|	|	+--	DialogButtonBox
#	|	|			buttons = List(DialogButton(...))
#	|	+--	(Dialog)
#	|		+--	MessageBox
#	|		|	|	buttons =
#	|		|	|	content =
#	|		|	|	details =
#	|		|	|	image =
#	|		|	|	text =
#	|		|	+--	about(parent, title, text)
#	|		|	+--	critical(parent, title, text, buttons=None)
#	|		|	+--	information(parent, title, text, buttons=None)
#	|		|	+--	question(parent, title, text, buttons=None)
#	|		|	+--	warning(parent, title, text, buttons=None)
#	|		+--	TaskDialogBody
#	|			|	padding =
#	|			+--	TaskDialogCommandArea
#	|			|	|	constraints =
#	|			|	+--	WIDGETS
#	|			+--	TaskDialogContentArea
#	|			|	+--	WIDGETS
#	|			+--	TaskDialogDetailsArea
#	|			|	|	visible =
#	|			|	+--	WIDGETS
#	|			+--	TaskDialogFootnoteArea
#	|			|	+--	WIDGETS
#	|			+--	TaskDialogIconArea
#	|			|		IconContent(...):
#	|			+--	TaskDialogInstructionArea
#	|				+--	WIDGETS
#	+--	DYNAMIC
#	|	+--	(Container)
#	|	|	|	constraints = (List())
#	|	|	|	padding =
#	|	|	+--	DynamicTemplate
#	|	|	|	args =
#	|	|	|	base =
#	|	|	+--	Include
#	|	|		objects =
#	|	+--	(Include)
#	|	|	+--	MappedView
#	|	+--	(Pattern)
#	|		+--	Conditional
#	|		|	|	condition =
#	|		|	+--	(Container)
#	|		+--	Looper
#	|			|	iterable =
#	|			|	items =
#	|			|	loop.index
#	|			|	loop.item
#	|			+--	(Container)
#	+--	EVENT
#	|	+--	(atom)
#	|		+--	DockItemEvent
#	|		|		type =
#	|		|		name =
#	|		+--	DragData
#	|		|		mime_data =
#	|		|		image =
#	|		+--	DropEvent
#	|		|		accept()
#	|		|		drop_action()
#	|		|		ignore()
#	|		|		is_accepted()
#	|		|		mime_data()
#	|		|		pos()
#	|		|		set_accepted(accepted)
#	|		+--	Signal
#	|				accept()
#	|				ignore()
#	+--	FOCUS
#	|	+--	(Container)
#	|			next_focus_child => (current):
#	|			previous_focus_child => (current):
#	+--	FUNCTION
#	|	+--	@d_func
#	|	|	+--	def new_func(self, params):
#	|	+--	new_func => (params):
#	|	+--	(Container)
#	|		+--	IPythonConsole
#	|				exit_requested ::
#	|				initial_ns =
#	+--	IMAGE
#	|	+--	(Atom)
#	|	|	+--	Icon
#	|	|	|		>IconImage
#	|	|	|		images = List(IconImage(...))
#	|	|	+--	IconImage
#	|	|	|		image =
#	|	|	|		mode =
#	|	|	|		state =
#	|	|	+--	Image
#	|	|			aspect_ratio_mode =
#	|	|			data =
#	|	|			format =
#	|	|			size =
#	|	|			transform_mode =
#	|	+--	(Container)
#	|		+--	ImageView
#	|		|		>Image
#	|		|		image << Image(data=...)
#	|		+--	MPLCanvas
#	|		|		>Figure
#	|		|		figure << Figure(...)
#	|		|		toolbar_visible =
#	|		+--	VTKCanvas
#	|				renderer =
#	+--	LIST
#	|	+--	(Container)
#	|		+--	ComboBox
#	|		|		index =
#	|		|		items =
#	|		+--	ObjectCombo
#	|				items =
#	|				selected =
#	|				to_string =
#	+--	LAYOUT
#	|	+--	CONTAINERS (those are)
#	|	|	+--	DockPane (see MainWindow)
#	|	|	|	|	allowed_dock_areas =
#	|	|	|	|	dock_area =
#	|	|	|	|	floating =
#	|	|	|	|	movable =
#	|	|	|	|	title =
#	|	|	|	+--	(Container)
#	|	|	+--	Form
#	|	|	|		column_spacing =
#	|	|	|		padding =
#	|	|	|		hug_height =
#	|	|	|		hug_width =
#	|	|	|		row_spacing =
#	|	|	+--	GroupBox
#	|	|	|		flat =
#	|	|	|		title =
#	|	|	|		title_align =
#	|	|	+--	HGroup
#	|	|	|		align_widths =
#	|	|	|		leading_spacer =
#	|	|	|		spacing =
#	|	|	|		trailing_spacer =
#	|	|	+--	VGroup
#	|	|		|	padding =
#	|	|		|	leading_spacer =
#	|	|		|	spacing =
#	|	|		|	trailing_spacer =
#	|	|		+--	(Container)
#	|	+--	(Container)
#	|		+--	ButtonGroup
#	|		+--	DockArea
#	|		|	|	apply_layout(layout)
#	|		|	|	dock_event ::
#	|		|	|	layout = (LayoutNode)
#	|		|	|	save_layout()
#	|		|	|	style =
#	|		|	+--	DockItem
#	|		|		|	alert(,,,,)
#	|		|		|	name =
#	|		|		|	stretch =
#	|		|		|	title =
#	|		|		+--	(Container)
#	|		+--	FlowArea
#	|		|	|	align =
#	|		|	|	direction =
#	|		|	|	horizontal_spacing =
#	|		|	|	margins =
#	|		|	|	vertical_spacing =
#	|		|	+--	FlowItem
#	|		|	|	|	align =
#	|		|	|	|	ortho_stretch =
#	|		|	|	|	preferred_size =
#	|		|	|	|	stretch =
#	|		|	|	+--	(Container)
#	|		|	+--	(Include)
#	|		|			objects =
#	|		+--	MdiArea
#	|		|	|	.cascade_mdi_windows()
#	|		|	|	.tile_mdi_windows()
#	|		|	+--	MdiWindow
#	|		|	|	|	title =
#	|		|	|	+--	(Container)
#	|		|	+--	(Include)
#	|		|			objects =
#	|		+--	Notebook
#	|		|	|	selected_tab =
#	|		|	|	tab_style =
#	|		|	|	tabs_closable =
#	|		|	|	tabs_movable =
#	|		|	+--	Page
#	|		|	|	|	closable =
#	|		|	|	|	name =
#	|		|	|	|	title =
#	|		|	|	|	tool_tip =
#	|		|	|	+--	Container
#	|		|	+--	(Include)
#	|		|			objects =
#	|		+--	ScrollArea
#	|		|	|	constraints =
#	|		|	|	horizontal_policy =
#	|		|	|	vertical_policy =
#	|		|	|	widget_resizable =
#	|		|	+--	(Container)
#	|		+--	Splitter
#	|		|	+--	SplitItem
#	|		|		|	collapsible =
#	|		|		|	stretch =
#	|		|		+--	(Container)
#	|		+--	Stack
#	|			+--	StackItem
#	+--	MENU
#	|	+--	(MenuBar) (or Widget)
#	|		+--	Menu
#	|			|	popup()
#	|			+--	Action
#	|			|	checkable =
#	|			|	separator =
#	|			|	icon =
#	|			|	text =
#	|			|	toggled ::
#	|			|	triggered ::
#	|			|	visible =
#	|			+--	(ActionGroup)
#	|			|	+--	Action
#	|			+--	(Menu)
#	+--	NUMERIC
#	|	+--	(Container)
#	|		|	constraints = (List())
#	|		|	padding =
#	|		+--	FloatField (stdlib)
#	|		|		maximum =
#	|		|		minimum =
#	|		|		allow_exponent =
#	|		|		value =
#	|		+--	IntField (stdlib)
#	|		|		maximum =
#	|		|		minimum =
#	|		|		value =
#	|		+--	ProgressBar
#	|		|		maximum =
#	|		|		minimum =
#	|		|		percentage =
#	|		|		value =
#	|		+--	Slider
#	|		|	|	maximum =
#	|		|	|	minimum =
#	|		|	|	tick_interval =
#	|		|	|	value =
#	|		|	+--	(SliderTransform)
#	|		|	|		maximum =
#	|		|	|		minimum =
#	|		|	|		precision =
#	|		|	|		value =
#	|		|	+--	(FloatTransform)
#	|		+--	SpinBox
#	|				maximum =
#	|				minimum =
#	|				value =
#	+--	PLUGIN
#	|	+--	PluginManifest
#	|		+--	ExtensionPoint
#	+--	STYLE
#	|	+--	(Container)
#	|	|	+--	Separator
#	|	+--	(StyleSheet) (using enamldef)
#	|		+--	Style
#	|			|	element = 'WIDGET'
#	|			|	object_name = (name =)
#	|			|	pseudo_class =
#	|			|		'active'
#	|			|		'bottom'
#	|			|		'checked'
#	|			|		'closable'
#	|			|		'closed'
#	|			|		'default'
#	|			|		'disabled'
#	|			|		'editable'
#	|			|		'enabled'
#	|			|		'exclusive'
#	|			|		'first'
#	|			|		'flat'
#	|			|		'floatable'
#	|			|		'focus'
#	|			|		'horizontal'
#	|			|		'hover'
#	|			|		'last'
#	|			|		'left'
#	|			|		'maximized'
#	|			|		'middle'
#	|			|		'minimized'
#	|			|		'movable'
#	|			|		'no-frame'
#	|			|		'non-exclusive'
#	|			|		'off'
#	|			|		'on'
#	|			|		'only-one'
#	|			|		'open'
#	|			|		'next-selected'
#	|			|		'pressed'
#	|			|		'previous-selected'
#	|			|		'read-only'
#	|			|		'right'
#	|			|		'selected'
#	|			|		'top'
#	|			|		'unchecked'
#	|			|		'vertical'
#	|			|		'window'
#	|			|	pseudo_element =
#	|			|		'add-line'
#	|			|		'add-page'
#	|			|		'chunk'
#	|			|		'close-button'
#	|			|		'corner'
#	|			|		'down-arrow'
#	|			|		'down-button'
#	|			|		'drop-down'
#	|			|		'float-button'
#	|			|		'groove'
#	|			|		'indicator'
#	|			|		'handle'
#	|			|		'icon'
#	|			|		'item'
#	|			|		'left-arrow'
#	|			|		'left-corner'
#	|			|		'menu-arrow'
#	|			|		'menu-button'
#	|			|		'menu-indicator'
#	|			|		'right-arrow'
#	|			|		'pane'
#	|			|		'right-corner'
#	|			|		'scroller'
#	|			|		'separator'
#	|			|		'sub-line'
#	|			|		'sub-page'
#	|			|		'tab'
#	|			|		'tab-bar'
#	|			|		'tear'
#	|			|		'tearoff'
#	|			|		'title'
#	|			|		'up-arrow'
#	|			|		'up-button'
#	|			|	style_class = 'FREE'
#	|			+--	Setter
#	|					field =
#	|						'alternate-background-color'
#	|						'background'
#	|						'background-clip'
#	|						'background-color'
#	|						'border'
#	|						'border-bottom'
#	|						'border-bottom-color'
#	|						'border-bottom-left-radius'
#	|						'border-bottom-right-radius'
#	|						'border-bottom-style'
#	|						'border-bottom-width'
#	|						'border-color'
#	|						'border-left'
#	|						'border-left-color'
#	|						'border-left-style'
#	|						'border-left-width'
#	|						'border-radius'
#	|						'border-right'
#	|						'border-right-color'
#	|						'border-right-style'
#	|						'border-right-width'
#	|						'border-style'
#	|						'border-top'
#	|						'border-top-color'
#	|						'border-top-left-radius'
#	|						'border-top-right-radius'
#	|						'border-top-style'
#	|						'border-top-width'
#	|						'border-width'
#	|						'bottom'
#	|						'color'
#	|						'font'
#	|						'font-family'
#	|						'font-size'
#	|						'font-style'
#	|						'font-weight'
#	|						'height'
#	|						'icon-size'
#	|						'left'
#	|						'line-edit-password-character'
#	|						'line-through'
#	|						'margin'
#	|						'margin-bottom'
#	|						'margin-left'
#	|						'margin-right'
#	|						'margin-top'
#	|						'max-height'
#	|						'max-width'
#	|						'min-height'
#	|						'min-width'
#	|						'overline'
#	|						'padding'
#	|						'padding-bottom'
#	|						'padding-left'
#	|						'padding-right'
#	|						'padding-top'
#	|						'position'
#	|						'right'
#	|						'selection-background-color'
#	|						'selection-color'
#	|						'spacing'
#	|						'subcontrol-origin'
#	|						'subcontrol-position'
#	|						'text-align'
#	|						'text-decoration'
#	|						'top'
#	|						'underline'
#	|						'width'
#	|					value =
#	|						('background')						Background
#	|						('background-clip')					Origin
#	|						('background-color')				Brush
#	|						('border')							Border
#	|						('border-bottom')					Border
#	|						('border-bottom-color')				Brush
#	|						('border-bottom-left-radius')		Radius
#	|						('border-bottom-right-radius')		Radius
#	|						('border-bottom-style')				Border_Style
#	|						('border-bottom-width')				Length
#	|						('border-color')					Box_Colors
#	|						('border-left')						Border
#	|						('border-left-color')				Brush
#	|						('border-left-style')				Border_Style
#	|						('border-left-width')				Length
#	|						('border-radius')					Radius
#	|						('border-right')					Border
#	|						('border-right-color')				Brush
#	|						('border-right-style')				Border_Style
#	|						('border-right-width')				Length
#	|						('border-style')					Border_Style
#	|						('border-top')						Border
#	|						('border-top-color')				Brush
#	|						('border-top-left-radius')			Radius
#	|						('border-top-right-radius')			Radius
#	|						('border-top-style')				Border_Style
#	|						('border-top-width')				Length
#	|						('border-width')					Box_Lengths
#	|						('bottom')							Length
#	|						('color')							Brush
#	|						('font')							Font
#	|						('font-family')						String
#	|						('font-size')						Font_Size
#	|						('font-style')						Font_Style
#	|						('font-weight')						Font_Weight
#	|						('height')							Length
#	|						('icon-size')						Length
#	|						('left')							Length
#	|						('line-edit-password-character')	Number
#	|						('margin')							Box_Lengths
#	|						('margin-bottom')					Length
#	|						('margin-left')						Length
#	|						('margin-right')					Length
#	|						('margin-top')						Length
#	|						('max-height')						Length
#	|						('max-width')						Length
#	|						('min-height')						Length
#	|						('min-width')						Length
#	|						('padding')							Box_Lengths
#	|						('padding-bottom')					Length
#	|						('padding-left')					Length
#	|						('padding-right')					Length
#	|						('padding-top')						Length
#	|						('position')						'relative' | 'absolute'
#	|						('right')							Length
#	|						('selection-background-color')		Brush
#	|						('selection-color')					Brush
#	|						('spacing')							Length
#	|						('subcontrol-origin')				Origin
#	|						('subcontrol-position')				Alignment
#	|						('text-align')						Alignment
#	|						('text-decoration')					'none' | 'underline' | 'overline' | 'line-through'
#	|						('top')								Length
#	|						('width')							Length
#	|
#	|	https://enaml.readthedocs.io/en/latest/dev_guides/stylesheets.html#list-of-field-types
#	|	Alignment		{ 'top' | 'bottom' | 'left' | 'right' | 'center' }*
#	|	Border_Style	'dashed' | 'dot-dash' | 'dot-dot-dash' | 'dotted' | 'double' | 'groove' | 'inset' | 'outset' | 'ridge' | 'solid' | 'none'
#	|	Origin			'margin' | 'border' | 'padding' | 'content'
#	|	Font_Stretch	'ultra-condensed' | 'extra-condensed' | 'condensed' | 'semi-condensed' | 'normal' | 'semi-expanded' | 'expanded' | 'extra-expanded' | 'ultra-expanded'
#	|	Font_Variant	'normal' | 'small-caps'
#	|	Color			{ rgb(r, g, b) | rgba(r, g, b, a) | hsv(h, s, v) | hsva(h, s, v, a) | #rrggbb | CSS_Color_Name }*
#	|	Number			integer | real
#	|	Gradient		( 'lineargradient' | 'radialgradient' )'(x1:' Number ', y1:' Number ', x2:' Number ', y2:' Number ', stop: ' Number Color ', stop: ' Number Color ')'
#	|	Length			Number ( 'px' | 'pt' | 'em' | 'ex' )
#	|	Font_Unit		Number ( 'in' | 'cm' | 'mm' | 'pt' | 'pc' | 'px' )
#	|	Font_Style		'normal' | 'italic' | 'oblique'
#	|	Font_Weight		'normal' | 'bold' | 100 | 200 | ... | 900
#	|	Brush			Color | Gradient
#	|	Box_Colors		Brush{1, 4}
#	|	Background		{ Brush | Alignment }*
#	|	Border			{ Border_Style | Length | Brush }*
#	|	Radius			Length{1, 2}
#	|	Box_Lengths		Length{1, 4}
#	|	Font_Size		Length | 'xx-small' | 'x-small' | 'small' | 'medium' | 'large' | 'x-large' | 'xx-large'
#	|	Font			( Font_Style | Font_Weight ){0, 2} Font_Size String
#	|
#	+--	TEXT
#	|	+--	(Container)
#	|		|	constraints = (List())
#	|		|	padding =
#	|		+--	Field
#	|		|	|	placeholder =
#	|		|	|	read_only =
#	|		|	|	text =
#	|		|	+--	(Menu)
#	|		|		|	context_menu =
#	|		|		|	text =
#	|		|		+--	(Action)
#	|		|			text <<
#	|		|			triggered ::
#	|		+--	Label
#	|		|		align =
#	|		|		constraints =
#	|		|		drag_start => ():
#	|		|		drag_end => (drag_data, result):
#	|		|		features =
#	|		|		foreground =
#	|		|		font =
#	|		|		hug_height =
#	|		|		style_class <<
#	|		|		text =
#	|		|		visible =
#	|		+--	MultilineField
#	|		|		constraints =
#	|		|		drag_enter => (event):
#	|		|		drop => (event):
#	|		|		enabled =
#	|		|		features =
#	|		|		font =
#	|		|		name =
#	|		|		read_only =
#	|		|		text =
#	|		+--	RegexField (stdlib)
#	|		+--	Scintilla
#	|			+--	ScintillaDocument
#	|			+--	(ScintillaIndicator)
#	|			+--	(ScintillaMarker)
#	+--	TIME
#	|	+--	(Container)
#	|		+--	Calendar
#	|		|		date >>
#	|		|		maximum =
#	|		+--	DateSelector
#	|		|		date >>
#	|		|		maximum =
#	|		|		minimum =
#	|		+--	DatetimeSelector
#	|		|		datetime >>
#	|		|		maximum =
#	|		|		minimum =
#	|		+--	TimeSelector
#	|				time >>
#	+--	WEB
#	|	+--	(Container)
#	|		+--	Html
#	|		|		source <<
#	|		+--	WebView
#	|				base_url =
#	|				html =
#	|				url =
#	+--	WINDOW
#		+--	(Window) (or Widget)
#			+--	MainWindow
#			|	|	closing ::
#			|	|	initial_size =
#			|	|	initialized ::
#			|	|	title =
#			|	+--	Container
#			|	|	constraints =
#			|	|	padding =
#			|	+--	(DockPane)
#			|	|	+--	(Container)
#			|	+--	MenuBar
#			|	|	+--	Menu
#			|	+--	StatusBar (using enamldef)
#			|	|	+--	StatusItem
#			|	|		+--	(WIDGETS)
#			|	+--	ToolBar
#			|		+--	Action
#			|		+--	(ActionGroup)
#			|		|	+--	Action
#			|		+--	(ToolButton)
#			+--	PopupView
#				|	anchor =
#				|	anchor_mode =
#				|	arrow_edge =
#				|	arrow_size =
#				|	background =
#				|	fade_in_duration =
#				|	fade_out_duration =
#				|	foreground =
#				|	offset =
#				|	parent_anchor =
#				|	show()
#				|	timeout =
#				|	window_type =
#				+--	(Container)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# AppLib : LiveEditorModel

from enaml.applib.live_editor_model import LiveEditorModel

	LiveEditorModel:
		model_text = Str()
		view_text = Str()
		model_item = Str()
		view_item = Str()
		model_filename = Str()
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A model which works in concert with the live editor panels
# << (Atom) :
lemodel = LiveEditorModel()

# <- (Str()) : The full text of the Python module which defines the model
lemodel.model_text = Str()

# <- (Str()) : The full text of the Enaml module which defines the view
lemodel.view_text = Str()

# <- (Str()) : The name of the target model class in the model module
lemodel.model_item = Str()

# <- (Str()) : The name of the target enamldef in the view module
lemodel.view_item = Str()

# <- (Str()) : An optional filename to associate with the model module
lemodel.model_filename = Str('__live_model__.py')

# <- (Str()) : An optional filename to associate with the view module
lemodel.view_filename = Str('__live_view__.enaml')

# -> (Typed(Atom)) : The instance of the user defined model, or None if no model could be created
compiled_model = lemodel.compiled_model

# -> (Typed(Object)) : The instance of the user defined view, or None if no view could be created
compiled_view = lemodel.compiled_view

# -> (Str()) : A string holding the traceback for any compilation and instantiation errors
traceback = lemodel.traceback

# Refresh the compiled model object
lemodel.refresh_model()

# Refresh the compiled view object
lemodel.refresh_view()

# Obtain autocompletion suggestions for the source text using jedi
#	source () :
#	position () :
# -> (list) : List of keywords (including ENAML_KEYWORDS)
lemodel.autocomplete(source, position)

# Relink the compiled view with the compiled model
lemodel.relink_view()

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Core : Conditional

from enaml.core.api import Conditional

	Conditional:
		condition = Bool()
		#
		self.destroy()
		self.pattern_items()
		self.refresh_items()
			#Pattern:
		self.destroy()
		self.child_node_intercept(nodes, key, f_locals)
		self.pattern_items()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A pattern object that represents conditional objects
# << (Pattern) :
cond = Conditional()

# <-> (Bool(True)) : The condition variable
#	True : a copy of the children will be inserted into the parent
#	False : the old copies will be destroyed
condition = cond.condition = condition

# A reimplemented destructor
cond.destroy()

# Get a list of items created by the pattern
# -> (List()) :
items = cond.pattern_items()

# Refresh the items of the pattern
cond.refresh_items()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Core : Declarative

from enaml.core.api import Declarative

	Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# The most base class of the Enaml declarative objects
# << (Object) :
decl = Declarative()

# <-> (Str()) : Export the 'name' attribute as a declarative member
name = decl.name = name

# <-> (Event()) : An event fired when an object is initialized
initialized = decl.initialized = initialized

# <-> (flag_property()) : A property which gets and sets the initialized flag
is_initialized = decl.is_initialized = is_initialized

# Initialize this object all of its children recursively
decl.initialize()

# An overridden destructor method for declarative cleanup
decl.destroy()

# An overridden child added event handler
#	child (Declarative) :
decl.child_added(child)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Core : d_

from enaml.core.api import d_

# Mark an Atom member as bindable from Enaml syntax
#	member (Member) : The atom member to mark as bindable from Enaml syntax
#	readable (bool, optional) : Whether the member is readable from Enaml syntax
#	writable (bool, optional) : Whether the member is writable from Enaml syntax
#	final (bool, optional) : Whether or not the member can be redefined from Enaml syntax using the 'attr' keyword
#		True, default : indicates that the member cannot be overridden
# -> (Member) :
member = d_(member, readable=True, writable=True, final=True)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Core : d_func

from enaml.core.api import d_func

# Mark a method as overridable from Enaml syntax
#	func (FunctionType) : The function to tag as declarative
# -> (func) : The original function tagged with the compiler metadata
func = d_func(func)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Core : DynamicTemplate

from enaml.core.api import DynamicTemplate

	DynamicTemplate:
		base = Typed(Template)
		args = Tuple()
		tags = Tuple(Str())
		startag = Str()
		data = Dict()
		tagged = Typed(ObjectDict, ())
		#
		self.initialize()
		self.destroy()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An object which dynamically instantiates a template
# << (Declarative) :
dyntempl = DynamicTemplate()

# <-> (Typed(Template)) : The template object to instantiate
base = dyntempl.base = base

# <-> (Tuple()) : The arguments to pass to the template
args = dyntempl.args = args

# <-> (Tuple(Str())) : The tags to apply to the return values of the template
tags = dyntempl.tags = tags

# <-> (Str()) : The tag to apply to overflow return items from the template
startag = dyntempl.startag = startag

# <-> (Dict()) : The data keywords to apply to the instantiated items
data = dyntempl.data = data

# <-> (Typed(ObjectDict, ())) : The object dictionary which maps tag name to tagged object
tagged = dyntempl.tagged = tagged

# A reimplemented initializer
dyntempl.initialize()

# A reimplemented destructor
dyntempl.destroy()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Core : Include

from enaml.core.api import Include

	Include:
		objects = ContainerList(Object)
		destroy_old = Bool(True)
		#
		self.initialize()
		self.destroy()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An object which dynamically inserts children into its parent
# << (Declarative) :
incl = Include()

# <-> (ContainerList(Object)) : The list of objects belonging to this Include
objects = incl.objects = objects

# <-> (Bool(True)) : A boolean flag indicating whether to destroy the old objects that are removed from the parent
destroy_old = incl.destroy_old = destroy_old

# A reimplemented initializer
incl.initialize()

# A reimplemented destructor
incl.destroy()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Core : Looper

from enaml.core.api import Looper

	Looper:
		iterable = Coerced(LooperIterable)
		items = List()
		#
		loop_index
		loop_item
		loop.index
		loop.item
		#
		self.destroy()
		self.pattern_items()
		self.refresh_items()
			#Pattern:
		self.destroy()
		self.child_node_intercept(nodes, key, f_locals)
		self.pattern_items()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A pattern object that repeats its children over an iterable
# << (Pattern) :
loop = Looper()

# <-> (Coerced(LooperIterable)) : The iterable to use when creating the items for the looper
iterable = loop.iterable = iterable

# <-> (List()) : The list of items created by the conditional
#	This list should not be manipulated directly by user code
items = loop.items

# A reimplemented destructor
loop.destroy()

# Get a list of items created by the pattern
# -> (List()) :
items = loop.pattern_items()

# Refresh the items of the pattern
loop.refresh_items()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Core : Object

from enaml.core.api import Object

	Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# The most base class of the Enaml object hierarchy
#	parent (Object or None) :
#		Object : The Object instance which is the parent of this object
#		None : if the object has no parent
# << (Atom) :
obj = Object(parent=None)

# <-> (Str()) : An optional name to give to this object to assist in finding it in the tree
name = obj.name = name

# <- (property) : The read-only property which returns the object parent
parent = obj.parent

# <- (property) : A read-only property which returns the object children
children = obj.children

# <- (flag_property(DESTROYED_FLAG)) : A property which gets and sets the destroyed flag
is_destroyed = obj.is_destroyed

# <-> (Event()) : An event fired when an object has been destroyed
destroyed = obj.destroyed = destroyed

# Destroy this object and all of its children recursively
obj.destroy()

# Set the parent for this object
#	parent (Object or None) :
#		Object : The Object instance to use for the parent
#		None : if this object should be unparented
obj.set_parent(parent)

# Insert children into this object at the given location
#	before (Object, int or None) :
#		Object, int : A child object or int to use as the marker for inserting the new children
#		None, not a child, or the int is not a valid index : the new children will be added to the end of the children
#	insert (iterable) : An iterable of Object children to insert into this object
obj.insert_children(before, insert)

# A method invoked when the parent of the object changes
#	old (Object or None) : The old parent of the object
#	new (Object or None) : The new parent of the object
obj.parent_changed(old, new)

# A method invoked when a child is added to the object (to be reimplemented)
#	child (Object) : The child added to this object
obj.child_added(child)

# A method invoked when a child is moved in the object (to be reimplemented)
#	child (Object) : The child moved in this object
obj.child_moved(child)

# A method invoked when a child is removed from the object (to be reimplemented)
#	child (Object) : The child removed from the object
obj.child_removed(child)

# Get the root object for this hierarchy
# -> (Object) : The top-most object in the hierarchy to which this object belongs
root = obj.root_object()

# Yield all of the objects in the tree, from this object down
#	depth_first (bool, optional) :
#		True : yield the nodes in depth first order
#		False : yield the nodes in breadth first order
obj.traverse(depth_first=False)

# Yield all of the objects in the tree, from this object up
#	root (Object, optional) : The object at which to stop traversal
obj.traverse_ancestors(root=None)

# Find the first object in the subtree with the given name
#	name (Str()) : The name of the object for which to search
#	regex (bool, optional) : Whether the given name is a regex string which should be matched against
# -> (Object or None) :
#		Object : The first object found with the given name
#		None : if no object is found with the given name
root = obj.find(name, regex=False)

# Find all objects in the subtree with the given name
#	name (Str()) : The name of the objects for which to search
#	regex (bool, optional) : Whether the given name is a regex string which should be matched against
# -> (List(Object)) :
#		List(Object) : The list of objects found with the given name
#		[] : if no objects are found with the given name
root = obj.find_all(name, regex=False)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Layout : ItemLayout

from enaml.layout.api import ItemLayout

	ItemLayout:
		name = Str()
		floating = Bool(False)
		geometry = Coerced(Rect, (-1, -1, -1, -1), coercer=_coerce_rect)
		linked = Bool(False)
		maximized = Bool(False)
		#
		self.__init__(name, **kwargs)
			#LayoutNode:
		self.children()
		self.traverse(depth_first=False)
		self.find(kind)
		self.find_all(kind)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout object for defining an item layout
#	name (Str()) :
# << (LayoutNode) :
itemlayout = ItemLayout(name)

# <-> (Str()) : The name of the DockItem to which this layout item applies
name = itemlayout.name = name

# <-> (Bool(False)) : Whether or not the item is floating
floating = itemlayout.floating = floating

# <-> (Coerced(Rect, (-1, -1, -1, -1), coercer=_coerce_rect)) : The geometry to apply to the item
geometry = itemlayout.geometry = geometry

# <-> (Bool(False)) : Whether or not the item is linked with its floating neighbors
linked = itemlayout.linked = linked

# <-> (Bool(False)) : Whether or not the item is maximized
maximized = itemlayout.maximized = maximized

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : TabLayout

from enaml.layout.api import TabLayout

	TabLayout:
		tab_position = Enum('top', 'bottom', 'left', 'right')
		index = Int(0)
		maximized = Bool(False)
		items = List(Coerced(ItemLayout))
		#
		self.__init__(*items, **kwargs)
		self.children()
			#LayoutNode:
		self.children()
		self.traverse(depth_first=False)
		self.find(kind)
		self.find_all(kind)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout object for defining tabbed dock layouts
#	items (List(Coerced(ItemLayout))) :
# << (LayoutNode) :
tablayout = TabLayout(*items)

# <-> (Enum('top', 'bottom', 'left', 'right')) : The position of the tabs in the tab layout
tab_position = tablayout.tab_position = tab_position

# <-> (Int(0)) : The index of the currently selected tab
index = tablayout.index = index

# <-> (Bool(False)) : Whether or not the tab layout is maximized
maximized = tablayout.maximized = maximized

# <-> (List(Coerced(ItemLayout))) : The list of item layouts to include in the tab layout
items = tablayout.items = items

# Get the list of children of the tab layout
# -> (List(Coerced(ItemLayout))) :
children = tablayout.children()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : SplitLayout

from enaml.layout.api import SplitLayout

	SplitLayout:
		orientation = Enum('horizontal', 'vertical')
		sizes = List(Int())
		items = List(Coerced(_SplitLayoutItem))
		#
		self.__init__(*items, **kwargs)
		self.children()
			#LayoutNode:
		self.children()
		self.traverse(depth_first=False)
		self.find(kind)
		self.find_all(kind)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout object for defining split dock layouts
#	items (List(Coerced(_SplitLayoutItem))) :
# << (LayoutNode) :
slayout = SplitLayout(*items)

# <-> (Enum('horizontal', 'vertical')) : The orientation of the split layout
orientation = slayout.orientation = orientation

# <-> (List(Int())) : The default sizes to apply to the items in the splitter
sizes = slayout.sizes = sizes

# <-> (List(Coerced(_SplitLayoutItem))) : This list of split layout items to include in the split layout
items = slayout.items = items

# Get the list of children of the split layout
# -> (List(Coerced(_SplitLayoutItem))) :
children = slayout.children()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : HSplitLayout

from enaml.layout.api import HSplitLayout

	HSplitLayout:
		self.__init__(*items, **kwargs)
			#SplitLayout:
		orientation = Enum('horizontal', 'vertical')
		sizes = List(Int())
		items = List(Coerced(_SplitLayoutItem))
		#
		self.__init__(*items, **kwargs)
		self.children()
			#LayoutNode:
		self.children()
		self.traverse(depth_first=False)
		self.find(kind)
		self.find_all(kind)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A split layout which defaults to 'horizonal' orientation
#	items (List(Coerced(_SplitLayoutItem))) :
# << (SplitLayout) :
hslayout = HSplitLayout(*items)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : VSplitLayout

from enaml.layout.api import VSplitLayout

	VSplitLayout:
		self.__init__(*items, **kwargs)
			#SplitLayout:
		orientation = Enum('horizontal', 'vertical')
		sizes = List(Int())
		items = List(Coerced(_SplitLayoutItem))
		#
		self.__init__(*items, **kwargs)
		self.children()
			#LayoutNode:
		self.children()
		self.traverse(depth_first=False)
		self.find(kind)
		self.find_all(kind)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A split layout which defaults to 'vertical' orientation
#	items (List(Coerced(_SplitLayoutItem))) :
# << (SplitLayout) :
vslayout = VSplitLayout(*items)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : DockBarLayout

from enaml.layout.api import DockBarLayout

	DockBarLayout:
		position = Enum('top', 'right', 'bottom', 'left')
		items = List(Coerced(ItemLayout))
		#
		self.__init__(*items, **kwargs)
		self.children()
			#LayoutNode:
		self.children()
		self.traverse(depth_first=False)
		self.find(kind)
		self.find_all(kind)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout object for defining a dock bar layout
#	items (List(Coerced(ItemLayout))) :
# << (LayoutNode) :
dblayout = DockBarLayout(*items)

# <-> (Enum('top', 'right', 'bottom', 'left')) : The position of the tool bar in its area
position = dblayout.position = position

# <-> (List(Coerced(ItemLayout))) : The list of item layouts to include in the tab layout
items = dblayout.items = items

# Get the list of children of the dock bar layout
# -> (List(Coerced(ItemLayout))) :
children = dblayout.children()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : AreaLayout

from enaml.layout.api import AreaLayout

	AreaLayout:
		items = Coerced(_AreaLayoutItem)
		dock_bars = List(DockBarLayout)
		floating = Bool(False)
		geometry = Coerced(Rect, (-1, -1, -1, -1), coercer=_coerce_rect)
		linked = Bool(False)
		maximized = Bool(False)
		#
		self.__init__(item=None, **kwargs)
		self.children()
			#LayoutNode:
		self.children()
		self.traverse(depth_first=False)
		self.find(kind)
		self.find_all(kind)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout object for defining a dock area layout
#	item (Coerced(_AreaLayoutItem)) :
# << (LayoutNode) :
alayout = AreaLayout(item=None)

# <-> (Coerced(_AreaLayoutItem)) : The main layout item to include in the area layout
items = alayout.items = items

# <-> (List(DockBarLayout)) : The dock bar layouts to include in the area layout
dock_bars = alayout.dock_bars = dock_bars

# <-> (Bool(False)) : Whether or not the area is floating
floating = alayout.floating = floating

# <-> (Coerced(Rect, (-1, -1, -1, -1), coercer=_coerce_rect)) : The geometry to apply to the area
geometry = alayout.geometry = geometry

# <-> (Bool(False)) : Whether or not the area is linked with its floating neighbors
linked = alayout.linked = linked

# <-> (Bool(False)) : Whether or not the area is maximized
maximized = alayout.maximized = maximized

# Get the list of children of the area layout
# -> (List(Coerced(_AreaLayoutItem)) + List(DockBarLayout)) :
children = alayout.children()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : DockLayout

from enaml.layout.api import DockLayout

	DockLayout:
		items = List(Coerced(_DockLayoutItem))
		#
		self.__init__(*items, **kwargs)
		self.children()
			#LayoutNode:
		self.children()
		self.traverse(depth_first=False)
		self.find(kind)
		self.find_all(kind)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# The layout object for defining toplevel dock layouts
#	items (List(Coerced(_DockLayoutItem))) :
# << (LayoutNode) :
dlayout = DockLayout(*items)

# <-> (List(Coerced(_DockLayoutItem))) : The layout items to include in the dock layout
items = dlayout.items = items

# Get the list of children of the dock layout
# -> (List(Coerced(_DockLayoutItem))) :
children = dlayout.children()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : DockLayoutWarning

from enaml.layout.api import DockLayoutWarning

	DockLayoutWarning:
			#UserWarning:

# A custom user warning for use with dock layouts
# << (UserWarning) :
dlwarning = DockLayoutWarning()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : InsertItem

from enaml.layout.api import InsertItem

	InsertItem:
		item = Str()
		target = Str()
		position = Enum('left', 'top', 'right', 'bottom')
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which inserts an item into a layout
# << (DockLayoutOp) :
iitem = InsertItem()

# <-> (Str()) : The name of the dock item to insert into the layout
item = iitem.item = item

# <-> (Str()) : The name of the dock item to use as the target location
target = iitem.target = target

# <-> (Enum('left', 'top', 'right', 'bottom')) : The position relative to the target at which to insert the item
position = iitem.position = position

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : InsertBorderItem

from enaml.layout.api import InsertBorderItem

	InsertBorderItem:
		item = Str()
		target = Str()
		position = Enum('left', 'top', 'right', 'bottom')
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which inserts an item into an area border
# << (DockLayoutOp) :
ibitem = InsertBorderItem()

# <-> (Str()) : The name of the dock item to insert into the layout
item = ibitem.item = item

# <-> (Str()) : The name of the dock item to use as the target location
target = ibitem.target = target

# <-> (Enum('left', 'top', 'right', 'bottom')) : The border position at which to insert the item
position = ibitem.position = position

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : InsertDockBarItem

from enaml.layout.api import InsertDockBarItem

	InsertDockBarItem:
		item = Str()
		target = Str()
		position = Enum('right', 'left', 'bottom', 'top')
		index = Int(-1)
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which inserts an item into a dock bar
# << (DockLayoutOp) :
idbitem = InsertDockBarItem()

# <-> (Str()) : The name of the dock item to insert into the layout
item = idbitem.item = item

# <-> (Str()) : The name of the dock item to use as the target location
target = idbitem.target = target

# <-> (Enum('right', 'left', 'bottom', 'top')) : The dock bar position at which to insert the item
position = idbitem.position = position

# <-> (Int(-1)) : The index at which to insert the dock bar item
index = idbitem.index = index

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : InsertTab

from enaml.layout.api import InsertTab

	InsertTab:
		item = Str()
		target = Str()
		index = Int(-1)
		tab_position = Enum('default', 'top', 'bottom', 'left', 'right')
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which inserts a tab into a tab group
# << (DockLayoutOp) :
itab = InsertTab()

# <-> (Str()) : The name of the dock item to insert into the tab group
item = itab.item = item

# <-> (Str()) : The name of an existing dock item in the tab group of interest
target = itab.target = target

# <-> (Int(-1)) : The index at which to insert the dock item
index = itab.index = index

# <-> (Enum('default', 'top', 'bottom', 'left', 'right')) : The position of the tabs for a newly created tab group
tab_position = itab.tab_position = tab_position

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : FloatItem

from enaml.layout.api import FloatItem

	FloatItem:
		item = Coerced(ItemLayout)
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which creates a floating dock item
# << (DockLayoutOp) :
fitem = FloatItem()

# <-> (Coerced(ItemLayout)) : The item layout to use when configuring the floating item
item = fitem.item = item

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : FloatArea

from enaml.layout.api import FloatArea

	FloatArea:
		area = Coerced(AreaLayout)
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which creates a new floating dock area
# << (DockLayoutOp) :
farea = FloatArea()

# <-> (Coerced(AreaLayout)) : The area layout to use when building the new dock area
area = farea.item = area

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : RemoveItem

from enaml.layout.api import RemoveItem

	RemoveItem:
		item = Str()
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which will remove an item from the layout
# << (DockLayoutOp) :
remitem = RemoveItem()

# <-> (Str()) : The name of the dock item to remove from the layout
item = remitem.item = item

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : ExtendItem

from enaml.layout.api import ExtendItem

	ExtendItem:
		item = Str()
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which extends an item in a dock bar
# << (DockLayoutOp) :
eitem = ExtendItem()

# <-> (Str()) : The name of the dock item to extend from its dock bar
item = eitem.item = item

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : RetractItem

from enaml.layout.api import RetractItem

	RetractItem:
		item = Str()
			#DockLayoutOp:
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A layout operation which extends an item in a dock bar
# << (DockLayoutOp) :
retitem = RetractItem()

# <-> (Str()) : The name of the dock item to extend from its dock bar
item = retitem.item = item

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : align

from enaml.layout.api import align

# Create a SequenceHelper with the given anchor object
#	anchor (Str()) : The name of the target anchor on the constrainable object
#	items (List()) : The constraint items to pass to the helper
#	config () : Additional keyword arguments to pass to the helper
# -> (SequenceHelper()) :
seqhelp = align(anchor, items, config)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : hbox

from enaml.layout.api import hbox

# Create a horizontal LinearBoxHelper object
#	items (List()) : The constraint items to pass to the helper
#	config () : Additional keyword arguments to pass to the helper
# -> (LinearBoxHelper()) :
lbhelp = hbox(items, config)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : vbox

from enaml.layout.api import vbox

# Create a vertical LinearBoxHelper object
#	items (List()) : The constraint items to pass to the helper
#	config () : Additional keyword arguments to pass to the helper
# -> (LinearBoxHelper()) :
lbhelp = vbox(items, config)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : horizontal

from enaml.layout.api import horizontal

# Create a left-to-right SequenceHelper object
#	items (List()) : The constraint items to pass to the helper
#	config () : Additional keyword arguments to pass to the helper
# -> (SequenceHelper()) :
seqhelp = horizontal(items, config)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : vertical

from enaml.layout.api import vertical

# Create a top-to-bottom SequenceHelper object
#	items (List()) : The constraint items to pass to the helper
#	config () : Additional keyword arguments to pass to the helper
# -> (SequenceHelper()) :
seqhelp = vertical(items, config)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : factory

from enaml.layout.api import factory

# Create a FactoryHelper with the given factory function
#	func (Callable()) : The callable which will generate the list of constraints
#	args (List()) : Additional positional arguments to pass to the factory
#	kwargs () : Additional keyword arguments to pass to the factory
# -> (FactoryHelper()) :
facthelp = factory(func, args, kwargs)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : grid

from enaml.layout.api import grid

# Create a GridHelper object with the given rows
#	rows () : Rows of identifier to use to build a grid
#	config () : Additional keyword arguments to pass to the helper
# -> (GridHelper()) :
gridhelp = grid(rows, config)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : spacer

from enaml.layout.api import spacer

spacer = LayoutSpacer(10)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : Box

from enaml.layout.api import Box

	Box:
		rect = Rect()
		size = Size()
		pos = Pos()
		#
		cls.coerce_type(item)
			#BaseBox:
		top = int
		right = int
		bottom = int
		left = int
		#
		cls.coerce_type(item)
		#
		self.__new__(top=None, right=None, bottom=None, left=None)
		self.__getnewargs__()
		self.__repr__()
			#tuple:

# A BaseBox implementation for integer values
# << (BaseBox) :
box = Box()

# -> (int) : The 'top' component of the box
top = box.top

# -> (int) : The 'right' component of the box
right = box.right

# -> (int) : The 'bottom' component of the box
bottom = box.bottom

# -> (int) : The 'left' component of the box
left = box.left

# -> (Rect()) : The equivalent Rect for this box
rect = box.rect

# -> (Size()) : The Size of this box
size = box.size

# -> (Pos()) : The Pos of this box
pos = box.pos

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : BoxF

from enaml.layout.api import BoxF

	BoxF:
		top = float
		right = float
		bottom = float
		left = float
		rectf = RectF()
		sizef = SizeF()
		posf = PosF()
		#
		cls.coerce_type(item)
			#BaseBox:
		top = int
		right = int
		bottom = int
		left = int
		#
		cls.coerce_type(item)
		#
		self.__new__(top=None, right=None, bottom=None, left=None)
		self.__getnewargs__()
		self.__repr__()
			#tuple:

# A BaseBox implementation for floating point values
# << (BaseBox) :
boxf = BoxF()

# -> (float) : The 'top' component of the box
topf = boxf.top

# -> (float) : The 'right' component of the box
rightf = boxf.right

# -> (float) : The 'bottom' component of the box
bottomf = boxf.bottom

# -> (float) : The 'left' component of the box
leftf = boxf.left

# -> (RectF()) : The equivalent Rect for this box
rectf = boxf.rect

# -> (SizeF()) : The Size of this box
sizef = boxf.size

# -> (PosF()) : The Pos of this box
posf = boxf.pos

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : Pos

from enaml.layout.api import Pos

	Pos:
		cls.coerce_type(item)
			#BasePos:
		x = int
		y = int
		#
		cls.coerce_type(item)
		#
		self.__new__(x=None, y=None)
		self.__getnewargs__()
		self.__repr__()
			#tuple:

# An implementation of BasePos for integer values
# << (BasePos) :
pos = Pos()

# -> (int) : The 'x' component of the position
x = pos.x

# -> (int) : The 'y' component of the position
y = pos.y

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : PosF

from enaml.layout.api import PosF

	PosF:
		x = float
		y = float
		#
		cls.coerce_type(item)
			#BasePos:
		x = int
		y = int
		#
		cls.coerce_type(item)
		#
		self.__new__(x=None, y=None)
		self.__getnewargs__()
		self.__repr__()
			#tuple:

# An implementation of BasePos of floating point values
# << (BasePos) :
posf = PosF()

# -> (float) : The 'x' component of the position
xf = posf.x

# -> (float) : The 'y' component of the position
yf = posf.y

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : Rect

from enaml.layout.api import Rect

	Rect:
		box = Box()
		pos = Pos()
		size = Size()
		#
		cls.coerce_type(item)
			#BaseRect:
		x = int
		y = int
		width = int
		height = int
		#
		cls.coerce_type(item)
		#
		self.__new__(x=None, y=None, width=None, height=None)
		self.__getnewargs__()
		self.__repr__()
			#tuple:

# A BaseRect implementation for integer values
# << (BaseRect) :
rect = Rect()

# -> (int) : The 'x' position component of the rect
x = rect.x

# -> (int) : The 'y' position component of the rect
y = rect.y

# -> (int) : The 'width' size component of the rect
width = rect.width

# -> (int) : The 'height' size component of the rect
height = rect.height

# -> (Box()) : The equivalent Box for this rect
box = rect.box

# -> (Pos()) : The position of the rect as a Pos object
pos = rect.pos

# -> (Size()) : The size of the rect as a Size object
size = rect.size

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : RectF

from enaml.layout.api import RectF

	RectF:
		x = float
		y = float
		width = float
		height = float
		box = BoxF()
		pos = PosF()
		size = SizeF()
		#
		cls.coerce_type(item)
			#BaseRect:
		x = int
		y = int
		width = int
		height = int
		#
		cls.coerce_type(item)
		#
		self.__new__(x=None, y=None, width=None, height=None)
		self.__getnewargs__()
		self.__repr__()
			#tuple:

# A BaseRect implementation for floating point values
# << (BaseRect) :
rectf = RectF()

# -> (float) : The 'x' position component of the rect
xf = rectf.x

# -> (float) : The 'y' position component of the rect
yf = rectf.y

# -> (float) : The 'width' size component of the rect
widthf = rectf.width

# -> (float) : The 'height' size component of the rect
heightf = rectf.height

# -> (BoxF()) : The equivalent Box for this rect
boxf = rectf.box

# -> (PosF()) : The position of the rect as a Pos object
posf = rectf.pos

# -> (SizeF()) : The size of the rect as a Size object
sizef = rectf.size

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : Size

from enaml.layout.api import Size

	Size:
		#
		cls.coerce_type(item)
			#BaseSize:
		width = int
		height = int
		#
		cls.coerce_type(item)
		#
		self.__new__(width=None, height=None)
		self.__getnewargs__()
		self.__repr__()
			#tuple:

# A BaseSize implementation for integer values
# << (BaseSize) :
size = Size()

# -> (int) : The 'width' component of the size
width = size.width

# -> (int) : The 'height' component of the size
height = size.height

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Layout : SizeF

from enaml.layout.api import SizeF

	SizeF:
		width = float
		height = float
		#
		cls.coerce_type(item)
			#BaseSize:
		width = int
		height = int
		#
		cls.coerce_type(item)
		#
		self.__new__(width=None, height=None)
		self.__getnewargs__()
		self.__repr__()
			#tuple:

# A BaseSize implementation for floating point values
# << (BaseSize) :
sizef = SizeF()

# -> (float) : The 'width' component of the size
widthf = sizef.width

# -> (float) : The 'height' component of the size
heightf = sizef.height

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Qt : QtApplication *always* needed

from enaml.qt.qt_application import QtApplication

app = QtApplication()
# Instantiate view and show it there
app.start()

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Scintilla : Scintilla

from enaml.scintilla.api import Scintilla

	Scintilla:
		autocomplete = Enum('none', 'all', 'document', 'apis')
		autocompletions = List(str)
		cursor_position = Tuple()
		document = Typed(ScintillaDocument, ())
		syntax = Enum(*SYNTAXES)
		theme = Typed(dict, ())
		settings = Typed(dict, ())
		zoom = Int()
		text_changed :: Event()
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		markers = List(ScintillaMarker)
		indicators = List(ScintillaIndicator)
		proxy = Typed(ProxyScintilla)
		#
		self.get_text()
		self.set_text(text)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A Scintilla text editing control
# << (Control) :
sci = Scintilla()

# <-> (Enum('none', 'all', 'document', 'apis')) : Enable autocompletion
autocomplete = sci.autocomplete = autocomplete

# <-> (List(str)) : Autocompletion values and call signatures
autocompletions = sci.autocompletions = autocompletions

# <-> (Tuple()) : Position of the cursor within the editor in the format (line, column)
cursor_position = sci.cursor_position = cursor_position

# <-> (Typed(ScintillaDocument, ())) : The scintilla document buffer to use in the editor
document = sci.document = document

# <-> (Enum(*SYNTAXES)) : The language syntax to apply to the document
syntax = sci.syntax = syntax

# <-> (Typed(dict, ())) : The theme to apply to the widget
theme = sci.theme = theme

# <-> (Typed(dict, ())) : The settings to apply to the widget
settings = sci.settings = settings

# <-> (Int()) : The zoom factor for the editor
zoom = sci.zoom = zoom

# <-> (Event()) : An event emitted when the text is changed
text_changed = sci.text_changed = text_changed

# <-> (set_default('ignore')) : Text Editors expand freely in height and width by default
hug_width = sci.hug_width = hug_width
hug_height = sci.hug_height = hug_height

# <-> (List(ScintillaMarker)) : Markers to display
markers = sci.markers = markers

# <-> (List(ScintillaIndicator)) : Indicators to display
indicators = sci.indicators = indicators

# <-> (Typed(ProxyScintilla)) : A reference to the ProxyScintilla object
proxy = sci.proxy = proxy

# Get the text in the current document
# -> (Str()) : The text in the current document
lbhelp = sci.get_text()

# Set the text in the current document
#	text (Str()) : The text to apply to the current document
sci.set_text(text)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Scintilla : ScintillaDocument

from enaml.scintilla.api import ScintillaDocument

	ScintillaDocument:
		uuid = Constant()
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An opaque class which represents a Scintilla text document
# << (Atom) :
doc = ScintillaDocument()

# <-> (Constant()) : A uuid which can be used as a handle by the toolkit backend
uuid = doc.uuid = uuid

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Scintilla : ScintillaIndicator

from enaml.scintilla.api import ScintillaIndicator

	ScintillaIndicator:
		start = Tuple()
		stop = Tuple()
		style = Enum('squiggle', 'plain', 'tt', 'diagonal', 'strike', 'hidden', 'box', 'round_box', 'straight_box', 'full_box', 'dashes', 'dots', 'squiggle_low', 'dot_box', 'thick_composition', 'thin_composition', 'text_color', 'triangle', 'triangle_character')
		color = Str("#000000")
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An indicator descriptor
# << (Atom) :
ind = ScintillaIndicator()

# <-> (Tuple()) : Starting cursor position of the indicator
start = ind.start = start

# <-> (Tuple()) : Stop cursor position of the indicator
stop = ind.stop = stop

# <-> (Enum(...)) : Indicator style
style = ind.style = style

# <-> (Str("#000000")) : Indicator foreground color
color = ind.color = color

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Scintilla : ScintillaMarker

from enaml.scintilla.api import ScintillaMarker

	ScintillaMarker:
		line = Int()
		image = Typed(Image)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A marker descriptor
# << (Atom) :
mark = ScintillaMarker()

# <-> (Int()) : Line of the marker
line = mark.line = line

# <-> (Typed(Image)) : Image to use
image = mark.image = image

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

from enaml.widgets.toolkit_object import ToolkitObject

	ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# <-> (Event()) : An event fired when an object's proxy is activated
activated = tkobj.activated = activated

# <-> (Typed(ProxyToolkitObject)) : A reference to the ProxyToolkitObject
proxy = tkobj.proxy = proxy

# <-> (flag_property(ACTIVE_PROXY_FLAG)) : A property which gets and sets the active proxy flag
proxy_is_active = tkobj.proxy_is_active = proxy_is_active

# A reimplemented initializer
tkobj.initialize()

# A reimplemented destructor
tkobj.destroy()

# A reimplemented child added event handler
#	child () :
tkobj.child_added(child)

# A reimplemented child removed event handler
#	child () :
tkobj.child_removed(child)

# Activate the proxy object tree
tkobj.activate_proxy()

# Initialize the proxy on the top-down activation pass
tkobj.activate_top_down()

# Initialize the proxy on the bottom-up activation pass
tkobj.activate_bottom_up()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Action

from enaml.widgets.api import Action

	Action:
		text = Str()
		tool_tip = Str()
		status_tip = Str()
		icon = Typed(Icon)
		checkable = Bool(False)
		checked = Bool(False)
		enabled = Bool(True)
		visible = Bool(True)
		separator = Bool(False)
		triggered :: Event(bool)
		toggled :: Event(bool)
		proxy = Typed(ProxyAction)
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A non visible widget used in a ToolBar or Menu
# << (ToolkitObject) :
action = Action()

# <-> (Str()) : The text label associate with the action
text = action.text = text

# <-> (Str()) : The tool tip text to use for this action
tool_tip = action.tool_tip = tool_tip

# <-> (Str()) : The text that is displayed in the status bar when the user hovers over the action
status_tip = action.status_tip = status_tip

# <-> (Typed(Icon)) : The icon to use for the Action
icon = action.icon = icon

# <-> (Bool(False)) : Whether or not the action can be checked
checkable = action.checkable = checkable

# <-> (Bool(False)) : Whether or not the action is checked
checked = action.checked = checked

# <-> (Bool(True)) : Whether or not the item representing the action is enabled
enabled = action.enabled = enabled

# <-> (Bool(True)) : Whether or not the item representing the action is visible
visible = action.visible = visible

# <-> (Bool(False)) : Whether or not the action should be treated as a separator
separator = action.separator = separator

# <-> (Event(bool)) : An event fired when the action is triggered by user interaction
triggered = action.triggered = triggered

# <-> (Event(bool)) : An event fired when a checkable action changes its checked state
toggled = action.toggled = toggled

# <-> (Typed(ProxyAction)) : A reference to the ProxyAction object
proxy = action.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ActionGroup

from enaml.widgets.api import ActionGroup

	ActionGroup:
		exclusive = Bool(True)
		enabled = Bool(True)
		visible = Bool(True)
		proxy = Typed(ProxyActionGroup)
		#
		self.actions()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A non visible widget used to group actions
# << (ToolkitObject) :
actiongrp = ActionGroup()

# <-> (Bool(True)) : Whether or not the actions in this group are exclusive
exclusive = actiongrp.exclusive = exclusive

# <-> (Bool(True)) : Whether or not the actions in this group are enabled
enabled = actiongrp.enabled = enabled

# <-> (Bool(True)) : Whether or not the actions in this group are visible
visible = actiongrp.visible = visible

# <-> (Typed(ProxyActionGroup)) : A reference to the ProxyActionGroup object
proxy = actiongrp.proxy = proxy

# Get Actions defined as children of the ActionGroup
# -> (List(Action)) :
actions = actiongrp.actions()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ButtonGroup

from enaml.widgets.api import ButtonGroup

	ButtonGroup:
		group_members = Typed(set, ())
		exclusive = Bool(True)
		proxy = Typed(ProxyButtonGroup)
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A way to declare a group of buttons
# << (ToolkitObject) :
buttongrp = ButtonGroup()

# <-> (Typed(set, ())) : Set of members belonging to the group
group_members = buttongrp.group_members = group_members

# <-> (Bool(True)) : Can only a single button in the group be checked at a time
exclusive = buttongrp.exclusive = exclusive

# <-> (Typed(ProxyButtonGroup)) : A reference to the ProxyButtonGroup object
proxy = buttongrp.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Calendar

from enaml.widgets.api import Calendar

	Calendar:
		proxy = Typed(ProxyCalendar)
			#BoundedDate:
		minimum = Typed(pydate, args=(1752, 9, 14))
		maximum = Typed(pydate, args=(7999, 12, 31))
		date = Typed(pydate, factory=pydate.today)
		proxy = Typed(ProxyBoundedDate)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A bounded date control which edits a Python datetime.date using a widget which resembles a calendar
# << (BoundedDate) :
calendar = Calendar()

# <-> (Typed(ProxyCalendar)) : A reference to the ProxyCalendar object
proxy = calendar.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : AbstractButton

from enaml.widgets.abstract_button import AbstractButton

	AbstractButton:
		text = Str()
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		group = ForwardTyped(ButtonGroup)
		checkable = Bool(False)
		checked = Bool(False)
		clicked :: Event(bool)
		toggled :: Event(bool)
		hug_width = set_default('weak')
		proxy = Typed(ProxyAbstractButton)
		#
		self.__init__(parent=None, **kwargs)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A base class for creating button-like controls
# << (Control) :
abtn = AbstractButton()

# <-> (Str()) : The text to use as the button's label
text = abtn.text = text

# <-> (Typed(Icon)) : The source url for the icon to use for the button
icon = abtn.icon = icon

# <-> (Coerced(Size, (-1, -1))) : The size to use for the icon
icon_size = abtn.icon_size = icon_size

# <-> (ForwardTyped(ButtonGroup)) : Group to which this button belongs to
group = abtn.group = group

# <-> (Bool(False)) : Whether or not the button is checkable
checkable = abtn.checkable = checkable

# <-> (Bool(False)) : Whether a checkable button is currently checked
checked = abtn.checked = checked

# <-> (Event(bool)) : Fired when the button is pressed then released
clicked = abtn.clicked = clicked

# <-> (Event(bool)) : Fired when a checkable button is toggled
toggled = abtn.toggled = toggled

# <-> (set_default('weak')) : Buttons hug their contents' width weakly by default
hug_width = abtn.hug_width = hug_width

# <-> (Typed(ProxyAbstractButton)) : A reference to the ProxyAbstractButton object
proxy = abtn.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : CheckBox

from enaml.widgets.api import CheckBox

	CheckBox:
		checkable = Bool(True)
		proxy = Typed(ProxyCheckBox)
			#AbstractButton:
		text = Str()
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		group = ForwardTyped(ButtonGroup)
		checkable = Bool(False)
		checked = Bool(False)
		clicked :: Event(bool)
		toggled :: Event(bool)
		hug_width = set_default('weak')
		proxy = Typed(ProxyAbstractButton)
		#
		self.__init__(parent=None, **kwargs)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An checkable button represented by a standard check box widget
# << (AbstractButton) :
chkbox = CheckBox()

# <-> (Bool(True)) : Check boxes are checkable by default
checkable = chkbox.checkable = checkable

# <-> (Typed(ProxyCheckBox)) : A reference to the ProxyPushButton object
proxy = chkbox.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ToolkitDialog

from enaml.widgets.toolkit_dialog import ToolkitDialog

	ToolkitDialog:
		title = Str()
		callback = Callable()
		destroy_on_close = Bool(True)
		accepted :: Event()
		rejected :: Event()
		finished :: Event(bool)
		result = Bool(False)
		proxy = Typed(ProxyToolkitDialog)
		#
		self.show()
		self.open()
		self.exec_()
		self.accept()
		self.reject()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A base class for defining toolkit dialogs
# << (ToolkitObject) :
tkdlg = ToolkitDialog()

# <-> (Str()) : The title of the dialog window.
title = tkdlg.title = title

# <-> (Callable()) : An optional callback which will be invoked when the dialog is closed
callback = tkdlg.callback = callback

# <-> (Bool(True)) : Whether to destroy the dialog widget on close
destroy_on_close = tkdlg.destroy_on_close = destroy_on_close

# <-> (Event()) : An event fired if the dialog is accepted. It has no payload.
accepted = tkdlg.accepted = accepted

# <-> (Event()) : An event fired when the dialog is rejected. It has no payload.
rejected = tkdlg.rejected = rejected

# <-> (Event(bool)) : An event fired when the dialog is finished
finished = tkdlg.finished = finished

# <-> (Bool(False)) : Whether or not the dialog was accepted by the user
result = tkdlg.result = result

# <-> (Typed(ProxyToolkitDialog)) : A reference to the ProxyToolkitDialog object.
proxy = tkdlg.proxy = proxy

# Open the dialog as a non modal dialog
tkdlg.show()

# pen the dialog as a window modal dialog
tkdlg.open()

# Open the dialog as an application modal dialog
# -> (bool) : Whether or not the dialog was accepted
result = tkdlg.exec_()

# Accept the current state and close the dialog
tkdlg.accept()

# Reject the current state and close the dialog
tkdlg.reject()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ColorDialog

from enaml.widgets.api import ColorDialog

	ColorDialog:
		current_color = ColorMember('white')
		show_alpha = Bool(True)
		show_buttons = Bool(True)
		selected_color = ColorMember()
		proxy = Typed(ProxyColorDialog)
		#
		cls.get_color(parent=None, **kwargs)
		cls.custom_count()
		cls.custom_color(index)
		cls.set_custom_color(index, color)
			#ToolkitDialog:
		title = Str()
		callback = Callable()
		destroy_on_close = Bool(True)
		accepted :: Event()
		rejected :: Event()
		finished :: Event(bool)
		result = Bool(False)
		proxy = Typed(ProxyToolkitDialog)
		#
		self.show()
		self.open()
		self.exec_()
		self.accept()
		self.reject()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A toolkit dialog that allows the user to select a color
# << (ToolkitDialog) :
colordlg = ColorDialog()

# <-> (ColorMember('white')) : The currently selected color of the dialog
current_color = colordlg.current_color = current_color

# <-> (Bool(True)) : Whether or not to show the alpha value control
show_alpha = colordlg.show_alpha = show_alpha

# <-> (Bool(True)) : Whether or not to show the dialog ok/cancel buttons
show_buttons = colordlg.show_buttons = show_buttons

# <-> (ColorMember()) : The color selected when the user clicks accepts the dialog
selected_color = colordlg.selected_color = selected_color

# <-> (Typed(ProxyColorDialog)) : A reference to the ProxyColorDialog object
proxy = colordlg.proxy = proxy

# A static method which launches a color dialog
#	parent (ToolkitObject or None) : The parent toolkit object for this dialog
#	kwargs () : Additional data to pass to the dialog constructor
# -> (Color or None) :
#		Color() : The selected color
#		None : if no color was selected
color = colordlg.get_color(parent=None, kwargs)

# Get the number of available custom colors
# -> (int) : The number of available custom colors
custom = colordlg.custom_count()

# Get the custom color for the given index
#	index (int) : The integer index of the custom color
# -> (Color) : The custom color for the index
color = colordlg.custom_color(index)

# Set the custom color for the given index
#	index (int) : The integer index of the custom color
#	color (Color()) : The custom color to set for the index
colordlg.set_custom_color(index, color)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ComboBox

from enaml.widgets.api import ComboBox

	ComboBox:
		items = List(Str())
		index = Int(-1)
		selected_item = Property(cached=True)
		editable = Bool(False)
		hug_width = set_default('weak')
		proxy = Typed(ProxyComboBox)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A drop-down list from which one item can be selected at a time
# << (Control) :
combobox = ComboBox()

# <-> (List(Str())) : The strings to display in the combo box
items = combobox.items = items

# <-> (Int(-1)) : The integer index of the currently selected item
index = combobox.index = index

# <-> (Property(cached=True)) : A read only cached property which returns the selected item
selected_item = combobox.selected_item = selected_item

# <-> (Bool(False)) : Whether the text in the combo box can be edited by the user
editable = combobox.editable = editable

# <-> (set_default('weak')) : A combo box hugs its width weakly by default
hug_width = combobox.hug_width = hug_width

# <-> (Typed(ProxyComboBox)) : A reference to the ProxyComboBox object
proxy = combobox.proxy = proxy

# The getter function for the selected item property
# -> (Str()) : If the index falls out of range, the selected item will be an empty string
selected_item = combobox.get_selected_item()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Container

from enaml.widgets.api import Container

	Container:
		share_layout = Bool(False)
		padding = Coerced(Box, (10, 10, 10, 10))
		resist_width = set_default('ignore')
		resist_height = set_default('ignore')
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyContainer)
		#
		self.widgets()
		self.visible_widgets()
		self.child_added(child)
		self.child_moved(child)
		self.child_removed(child)
		self.layout_constraints(child)
			#Frame:
		border = Typed(Border)
		proxy = Typed(ProxyFrame)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A Frame subclass which provides child layout functionality
# << (Frame, ContentsConstrainableMixin) :
container = Container()

# <-> (Bool(False)) : A boolean which indicates whether or not to allow the layout ownership of this container to be transferred to an ancestor
share_layout = container.share_layout = share_layout

# <-> (Coerced(Box, (10, 10, 10, 10))) : A box object which holds the padding for this component
padding = container.padding = padding

# <-> (set_default('ignore')) : A Container does not generate constraints for its size hint by default
resist_width = container.resist_width = resist_width
resist_height = container.resist_height = resist_height
hug_width = container.hug_width = hug_width
hug_height = container.hug_height = hug_height

# <-> (Typed(ProxyContainer)) : A reference to the ProxyContainer object
proxy = container.proxy = proxy

# Get the child ConstraintsWidgets defined on the container
# -> (List(ConstraintsWidget)) :
widgets = container.widgets()

# Get the visible child ConstraintsWidgets on the container
# -> (List(ConstraintsWidget)) :
vis_widgets = container.visible_widgets()

# Handle the child added event on the container
#	child (ConstraintsWidget) :
container.child_added(child)

# Handle the child moved event on the container
#	child (ConstraintsWidget) :
container.child_moved(child)

# Handle the child removed event on the container
#	child (ConstraintsWidget) :
container.child_removed(child)

# The constraints generation for a Container
# -> (List(ConstraintsWidget)) :
container.layout_constraints(child)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : DateSelector

from enaml.widgets.api import DateSelector

	DateSelector:
		date_format = Str()
		calendar_popup = Bool(False)
		hug_width = set_default('ignore')
		proxy = Typed(ProxyDateSelector)
			#BoundedDate:
		minimum = Typed(pydate, args=(1752, 9, 14))
		maximum = Typed(pydate, args=(7999, 12, 31))
		date = Typed(pydate, factory=pydate.today)
		proxy = Typed(ProxyBoundedDate)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget to edit a Python datetime.date object
# << (BoundedDate) :
dselect = DateSelector()

# <-> (Str()) : A python date format string to format the date for display
date_format = dselect.date_format = date_format

# <-> (Bool(False)) : Whether to use a calendar popup for selecting the date
calendar_popup = dselect.calendar_popup = calendar_popup

# <-> (set_default('ignore')) : A date selector expands freely in width by default
hug_width = dselect.hug_width = hug_width

# <-> (Typed(ProxyDateSelector)) : A reference to the ProxyDateSelector object
proxy = dselect.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : DatetimeSelector

from enaml.widgets.api import DatetimeSelector

	DatetimeSelector:
		datetime_format = Str()
		calendar_popup = Bool(False)
		hug_width = set_default('ignore')
		proxy = Typed(ProxyDatetimeSelector)
			#BoundedDatetime:
		minimum = Typed(pydatetime, args=(1752, 9, 14, 0, 0, 0, 0))
		maximum = Typed(pydatetime, args=(7999, 12, 31, 23, 59, 59, 999000))
		datetime = Typed(pydatetime, factory=pydatetime.now)
		proxy = Typed(ProxyBoundedDatetime)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget to edit a Python datetime.datetime object
# << (BoundedDatetime) :
dtselect = DatetimeSelector()

# <-> (Str()) : A python date format string to format the datetime
datetime_format = dtselect.datetime_format = datetime_format

# <-> (Bool(False)) : Whether to use a calendar popup for selecting the date
calendar_popup = dtselect.calendar_popup = calendar_popup

# <-> (set_default('ignore')) : A datetime selector expands freely in width by default
hug_width = dtselect.hug_width = hug_width

# <-> (Typed(ProxyDatetimeSelector)) : A reference to the ProxyDateSelector object
proxy = dtselect.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Dialog

from enaml.widgets.api import Dialog

	Dialog:
		result = Bool(False)
		finished :: Event(bool)
		accepted :: Event()
		rejected :: Event()
		modality = set_default('application_modal')
		proxy = Typed(ProxyDialog)
		#
		self.exec_()
		self.done(result)
		self.accept()
		self.reject()
			#Window:
		windows = set()
		title = Str()
		initial_position = Coerced(Pos, (-1, -1))
		initial_size = Coerced(Size, (-1, -1))
		modality = Enum('non_modal', 'application_modal', 'window_modal')
		destroy_on_close = Bool(True)
		icon = Typed(Icon)
		always_on_top = Bool(False)
		closing :: Event(CloseEvent)
		closed :: Event()
		visible = set_default(False)
		proxy = Typed(ProxyWindow)
		#
		self.initialize()
		self.destroy()
		self.central_widget()
		self.position()
		self.set_position(pos)
		self.size()
		self.set_size(size)
		self.geometry()
		self.set_geometry(rect)
		self.frame_geometry()
		self.maximize()
		self.is_maximized()
		self.minimize()
		self.is_minimized()
		self.restore()
		self.send_to_front()
		self.send_to_back()
		self.activate_window()
		self.center_on_screen()
		self.center_on_widget(other)
		self.close()
		self.show()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A top-level Window class for creating dialogs
# << (Window) :
dlg = Dialog()

# <-> (Bool(False)) : The result of the dialog
result = dlg.result = result

# <-> (Event(bool)) : An event fired when the dialog is finished
finished = dlg.finished = finished

# <-> (Event()) : An event fired when the dialog is accepted
accepted = dlg.accepted = accepted

# <-> (Event()) : An event fired when the dialog is rejected
rejected = dlg.rejected = rejected

# <-> (set_default('application_modal')) : Dialogs are application modal by default
modality = dlg.modality = modality

# <-> (Typed(ProxyDialog)) : A reference to the ProxyDialog object
proxy = dlg.proxy = proxy

# Launch the dialog as a modal window
# -> (Bool()) : The result value of the dialog
result = dlg.exec_()

# Close the dialog and set the result value
#	result (Bool()) : The result value for the dialog
dlg.done(result)

# Close the dialog and set the result to True
dlg.accept()

# Close the dialog and set the result to False
dlg.reject()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : DockArea

from enaml.widgets.api import DockArea

	DockArea:
		layout = Coerced(DockLayout, ())
		tab_position = Enum('top', 'bottom', 'left', 'right')
		live_drag = Bool(True)
		style = Str('vs-2010')
		dock_events_enabled = Bool(False)
		dock_event :: Event(DockEvent)
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyDockArea)
		#
		self.initialized()
		self.dock_items()
		self.save_layout()
		self.apply_layout(layout)
		self.update_layout(ops)
		self.suppress_dock_events(ops)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A component which arranges dock item children
# << (ConstraintsWidget) :
darea = DockArea()

# <-> (Coerced(DockLayout, ())) : The layout of dock items for the area
layout = darea.layout = layout

# <-> (Enum('top', 'bottom', 'left', 'right')) : The default tab position for newly created dock tabs
tab_position = darea.tab_position = tab_position

# <-> (Bool(True)) : Whether the dock items resize as a dock splitter is being dragged
live_drag = darea.live_drag = live_drag

# <-> (Str('vs-2010')) : The name of the registered style to apply to the dock area
style = darea.style = style

# <-> (Bool(False)) : Whether or not dock events are enabled for the area
dock_events_enabled = darea.dock_events_enabled = dock_events_enabled

# <-> (Event(DockEvent)) : An event emitted when a dock event occurs in the dock area
dock_event = darea.dock_event = dock_event

# <-> (set_default('ignore')) : A Stack expands freely in height and width by default
hug_width = darea.hug_width = hug_width
hug_height = darea.hug_height = hug_height

# <-> (Typed(ProxyDockArea)) : A reference to the ProxyStack widget
proxy = darea.proxy = proxy

# This method ensures the internal style sheet is created
darea.initialized()

# Get the dock items defined on the stack
# -> (List(DockItem)) :
ditems = darea.dock_items()

# Save the current layout state of the dock area
# -> (DockLayout) :
dlayout = darea.save_layout()

# Apply a new layout to the dock area
#	layout (DockLayout) : The dock layout to apply to the dock area
# -> () :
dlayout = darea.apply_layout(layout)

# Update the layout configuration using layout operations
#	ops (DockLayoutOp or iterable) : A single DockLayoutOp instance or an iterable of the same
dlayout = darea.update_layout(ops)

# A context manager which supresses dock events
darea.suppress_dock_events(ops)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : DockItem

from enaml.widgets.api import DockItem

	DockItem:
		title = Str()
		title_editable = Bool(False)
		title_bar_visible = Bool(True)
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		stretch = Range(low=0, value=1)
		closable = Bool(True)
		title_bar_right_clicked :: Event()
		closing :: Event(CloseEvent)
		closed :: Event()
		proxy = Typed(ProxyDockItem)
		#
		self.dock_widget()
		self.alert(level, on=250, off=250, repeat=4, persist=False)
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which can be docked in a DockArea
# << (Widget) :
ditem = DockItem()

# <-> (Str()) : The title to use in the title bar
title = ditem.title = title

# <-> (Bool(False)) : Whether or the not the title is user editable
title_editable = ditem.title_editable = title_editable

# <-> (Bool(True)) : Whether or not the title bar is visible
title_bar_visible = ditem.title_bar_visible = title_bar_visible

# <-> (Typed(Icon)) : The icon to use in the title bar
icon = ditem.icon = icon

# <-> (Coerced(Size, (-1, -1))) : The size to use for the icon in the title bar
icon_size = ditem.icon_size = icon_size

# <-> (Range(low=0, value=1)) : The stretch factor for the item when docked in a splitter
stretch = ditem.stretch = stretch

# <-> (Bool(True)) : Whether or not the dock item is closable via a close button
closable = ditem.closable = closable

# <-> (Event()) : An event emitted when the title bar is right clicked
title_bar_right_clicked = ditem.title_bar_right_clicked = title_bar_right_clicked

# <-> (Event(CloseEvent)) : An event fired when the user request the dock item to be closed
closing = ditem.closing = closing

# <-> (Event()) : An event emitted when the dock item is closed
closed = ditem.closed = closed

# <-> (Typed(ProxyDockItem)) : A reference to the ProxyDockItem object
proxy = ditem.proxy = proxy

# Get the dock widget defined for the dock pane
# -> (Container) :
cont = ditem.dock_widget()

# Set the alert level on the dock item
#	level (Str()) : The alert level token to apply to the dock item
#	on (int) : The duration of the 'on' cycle, in ms
#		-1 : always on
#	off (int) : The duration of the 'off' cycle, in ms
#	repeat (int) : The number of times to repeat the on-off cycle
#	persist (bool) : Whether to leave the alert in the 'on' state when the cycles finish
ditem.alert(level, on=250, off=250, repeat=4, persist=False)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : DockPane

from enaml.widgets.api import DockPane

	DockPane:
		title = Str()
		title_bar_visible = Bool(True)
		title_bar_orientation = num('horizontal', 'vertical')
		closable = Bool(True)
		movable = Bool(True)
		floatable = Bool(True)
		floating = Bool(False)
		dock_area = Enum('left', 'right', 'top', 'bottom')
		allowed_dock_areas = List(Enum('left', 'right', 'top', 'bottom', 'all'), ['all'],)
		closed :: Event()
		proxy = Typed(ProxyDockPane)
		#
		self.dock_widget()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which can be docked in a MainWindow
# << (Widget) :
dpane = DockPane()

# <-> (Str()) : The title to use in the title bar
title = dpane.title = title

# <-> (Bool(True)) : Whether or not the title bar is visible
title_bar_visible = dpane.title_bar_visible = title_bar_visible

# <-> (Enum('horizontal', 'vertical')) : The orientation of the title bar
title_bar_orientation = dpane.title_bar_orientation = title_bar_orientation

# <-> (Bool(True)) : Whether or not the dock pane is closable via a close button
closable = dpane.closable = closable

# <-> (Bool(True)) : Whether or not the dock pane is movable by the user
movable = dpane.movable = movable

# <-> (Bool(True)) : Whether or not the dock can be floated as a separate window
floatable = dpane.floatable = floatable

# <-> (Bool(False)) : A boolean indicating whether or not the dock pane is floating
floating = dpane.floating = floating

# <-> (Enum('left', 'right', 'top', 'bottom')) : The dock area in the MainWindow where the pane is docked
dock_area = dpane.dock_area = dock_area

# <-> (List(Enum('left', 'right', 'top', 'bottom', 'all'), ['all'],)) : The dock areas in the MainWindow where the pane can be docked by the user
allowed_dock_areas = dpane.allowed_dock_areas = allowed_dock_areas

# <-> (Event()) : An event fired when the user closes the pane by clicking on the dock pane's close button
closed = dpane.closed = closed

# <-> (Typed(ProxyDockPane)) : A reference to the ProxyDockPane object
proxy = dpane.proxy = proxy

# Get the dock widget defined for the dock pane
# -> (Container) :
cont = ditem.dock_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : DualSlider

from enaml.widgets.api import DualSlider

	DualSlider:
		minimum = Int(0)
		maximum = Int(100)
		low_value = Int()
		high_value = Int()
		tick_position = TickPosition('bottom')
		tick_interval = Range(low=0)
		orientation = Enum('horizontal', 'vertical')
		auto_hug = Bool(True)
		proxy = Typed(ProxySeparator)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A simple dual slider widget
# << (Control) :
dualslid = DualSlider()

# <-> (Int(0)) : The minimum slider value
minimum = dualslid.minimum = minimum

# <-> (Int(100)) : The maximum slider value
maximum = dualslid.maximum = maximum

# <-> (Int()) : The low position value of the DualSlider
low_value = dualslid.low_value = low_value

# <-> (Int()) : The high position value of the DualSlider
high_value = dualslid.high_value = high_value

# <-> (TickPosition('bottom')) :  A TickPosition enum value indicating how to display the tick marks
tick_position = dualslid.tick_position = tick_position

# <-> (Range(low=0)) : The interval to place between slider tick marks in value units (as opposed to pixels
tick_interval = dualslid.tick_interval = tick_interval

# <-> (Enum('horizontal', 'vertical')) : The orientation of the slider
orientation = dualslid.orientation = orientation

# <-> (Bool(True)) :
#		True : value is updated while sliding
#		False : only updated when the slider is released
#tracking = dualslid.tracking = tracking

# <-> (Bool(True)) : Whether or not to automatically adjust the 'hug_width' and 'hug_height' values based on the value of 'orientation'
auto_hug = dualslid.auto_hug = auto_hug

# <-> (Typed(ProxySeparator)) : A reference to the ProxySeparator object
proxy = dualslid.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Field

from enaml.widgets.api import Field

	Field:
		text = Str()
		mask = Str()
		validator = Typed(Validator)
		submit_triggers = List(Enum('lost_focus', 'return_pressed', 'auto_sync'), ['lost_focus', 'return_pressed'])
		sync_time = Int(300)
		placeholder = Str()
		echo_mode = Enum('normal', 'password', 'silent')
		max_length = Int(0)
		read_only = Bool(False)
		text_align = Enum('left', 'right', 'center')
		hug_width = set_default('ignore')
		proxy = Typed(ProxyField)
		#
		self.field_text()
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A single line editable text widget
# << (Control) :
field = Field()

# <-> (Str()) : The unicode text to display in the field
text = field.text = text

# <-> (Str()) : The mask to use for text input
mask = field.mask = mask

# <-> (Typed(Validator)) : The validator to use for this field
validator = field.validator = validator

# <-> (List(Enum('lost_focus', 'return_pressed', 'auto_sync'), ['lost_focus', 'return_pressed'])) : The list of actions which should cause the client to submit its text to the server for validation and update
submit_triggers = field.submit_triggers = submit_triggers

# <-> (Int(300)) : Time in ms after which the client submit its text to the server for validation and update when the user stop typing
sync_time = field.sync_time = sync_time

# <-> (Str()) : The grayed-out text to display if the field is empty and the widget doesn't have focus
placeholder = field.placeholder = placeholder

# <-> (Enum('normal', 'password', 'silent')) : How to display the text in the field
echo_mode = field.echo_mode = echo_mode

# <-> (Int(0)) : The maximum length of the field in characters
max_length = field.max_length = max_length

# <-> (Bool(False)) : Whether or not the field is read only. Defaults to False
read_only = field.read_only = read_only

# <-> (Enum('left', 'right', 'center')) : Alignment for the text inside the field. Defaults to 'left'
text_align = field.text_align = text_align

# <-> (set_default('ignore')) : How strongly a component hugs it's contents' width
hug_width = field.hug_width = hug_width

# <-> (Typed(ProxyField)) : A reference to the ProxyField object
proxy = field.proxy = proxy

# Get the text stored in the field control
# -> (Str()) : The unicode text stored in the field (may be different than that stored in the 'text' attribute)
text = field.field_text()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : FileDialog

from enaml.widgets.api import FileDialog

	FileDialog:
		title = Str()
		mode = Enum('open_file', 'open_files', 'save_file', 'directory')
		path = Str()
		paths = List(Str())
		filters = List(Str())
		selected_filter = Str()
		native_dialog = Bool(True)
		result = Enum('rejected', 'accepted')
		callback = Callable()
		accepted :: Event(str)
		rejected :: Event()
		closed :: Event()
		destroy_on_close = Bool(True)
		proxy = Typed(ProxyFileDialog)
		#
		self.open()
		self.exec_()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A dialog widget that allows the user to open and save files and directories
# << (ToolkitObject) :
filedlg = FileDialog()

# <-> (Str()) : The title to use for the dialog
title = filedlg.title = title

# <-> (Enum('open_file', 'open_files', 'save_file', 'directory')) : The mode of the dialog
mode = filedlg.mode = mode

# <-> (Str()) : The selected path in the dialog
path = filedlg.path = path

# <-> (List(Str())) : The list of selected paths in the dialog
paths = filedlg.paths = paths

# <-> (List(Str())) : The string filters used to restrict the user's selections
filters = filedlg.filters = filters

# <-> (Str()) : The selected filter from the list of filters
selected_filter = filedlg.selected_filter = selected_filter

# <-> (Bool(True)) : Whether to use a platform native dialog, when available
native_dialog = filedlg.native_dialog = native_dialog

# <-> (Enum('rejected', 'accepted')) : An enum indicating if the dialog was accepted or rejected by the user
result = filedlg.result = result

# <-> (Callable()) : An optional callback which will be invoked when the dialog is closed
callback = filedlg.callback = callback

# <-> (Event(str)) : An event fired if the dialog is accepted
accepted = filedlg.accepted = accepted

# <-> (Event()) : An event fired when the dialog is rejected
rejected = filedlg.rejected = rejected

# <-> (Event()) : An event fired when the dialog is closed
closed = filedlg.closed = closed

# <-> (Bool(True)) : Whether to destroy the dialog widget on close
destroy_on_close = filedlg.destroy_on_close = destroy_on_close

# <-> (Typed(ProxyFileDialog)) : A reference to the ProxyFileDialog object
proxy = filedlg.proxy = proxy

# Open the dialog in a non-blocking fashion
filedlg.open()

# Open the dialog in a blocking fashion
# -> (Str()) : The path selected by the user, or an empty string if the dialog is cancelled
path = filedlg.exec_()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : FileDialogEx

from enaml.widgets.api import FileDialogEx

	FileDialogEx:
		file_mode = Enum('any_file', 'existing_file', 'existing_files', 'directory')
		show_dirs_only = Bool(False)
		current_path = Str()
		selected_paths = List(Str())
		name_filters = List(Str())
		selected_name_filter = Str()
		proxy = Typed(ProxyFileDialogEx)
		#
		cls.get_existing_directory(parent=None, **kwargs)
		cls.get_open_file_name(parent=None, **kwargs)
		cls.get_open_file_names(parent=None, **kwargs)
		cls.get_save_file_name(parent=None, **kwargs)
		#
		self.exec_native()
			#ToolkitDialog:
		title = Str()
		callback = Callable()
		destroy_on_close = Bool(True)
		accepted :: Event()
		rejected :: Event()
		finished :: Event(bool)
		result = Bool(False)
		proxy = Typed(ProxyToolkitDialog)
		#
		self.show()
		self.open()
		self.exec_()
		self.accept()
		self.reject()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A toolkit dialog for getting file and directory names
# << (ToolkitDialog) :
filedlgex = FileDialogEx()

# <-> (Enum('any_file', 'existing_file', 'existing_files', 'directory')) : The file mode of the dialog
file_mode = filedlgex.file_mode = file_mode

# <-> (Bool(False)) : Whether or not to only show directories
show_dirs_only = filedlgex.show_dirs_only = show_dirs_only

# <-> (Str()) : The currently selected path in the dialog
current_path = filedlgex.current_path = current_path

# <-> (List(Str())) : The paths selected by the user when the dialog is accepted
selected_paths = filedlgex.selected_paths = selected_paths

# <-> (List(Str())) : The name filters used to restrict the available files
name_filters = filedlgex.name_filters = name_filters

# <-> (Str()) : The selected name filter from the list of name filters
selected_name_filter = filedlgex.selected_name_filter = selected_name_filter

# <-> (Typed(ProxyFileDialogEx)) : A reference to the ProxyFileDialogEx object
proxy = filedlgex.proxy = proxy

# Get an existing directory on the filesystem
#		parent (ToolkitObject or None) : The parent toolkit object for this dialog
#		kwargs () : Additional data to pass to the dialog constructor
# -> (Str()) : The user selected directory path
#		'' : if no directory was selected
path = filedlgex.get_existing_directory(parent=None, kwargs)

# Get the file name for an open file dialog
#		parent (ToolkitObject or None) : The parent toolkit object for this dialog
#		kwargs () : Additional data to pass to the dialog constructor
# -> (Str()) : The user selected file name
#		'' : if no file name was selected
path = filedlgex.get_open_file_name(parent=None, kwargs)

# Get the file names for an open files dialog
#		parent (ToolkitObject or None) : The parent toolkit object for this dialog
#		kwargs () : Additional data to pass to the dialog constructor
# -> (List(Str())) : The user selected file names
#		[] : if no file names were selected
paths = filedlgex.get_open_file_names(parent=None, kwargs)

# Get the file name for a save file dialog
#		parent (ToolkitObject or None) : The parent toolkit object for this dialog
#		kwargs () : Additional data to pass to the dialog constructor
# -> (Str()) : The user selected file name
#		'' : if no file name was selected
path = filedlgex.get_save_file_name(parent=None, kwargs)

# Open the dialog using a native OS dialog if available
# -> (Bool()) : Whether or not the dialog was accepted
accepted = filedlgex.exec_native()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : FlowArea

from enaml.widgets.api import FlowArea

	FlowArea:
		direction = Enum('left_to_right', 'right_to_left', 'top_to_bottom', 'bottom_to_top')
		align = Enum('leading', 'trailing', 'center', 'justify')
		horizontal_spacing = Range(low=0, value=10)
		vertical_spacing = Range(low=0, value=10)
		margins = Coerced(Box, (10, 10, 10, 10))
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyFlowArea)
		#
		self.flow_items()
			#Frame:
		border = Typed(Border)
		proxy = Typed(ProxyFrame)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which lays out its children in flowing manner, wrapping around at the end of the available space
# << (Frame) :
farea = FlowArea()

# <-> (Enum('left_to_right', 'right_to_left', 'top_to_bottom', 'bottom_to_top')) : The flow direction of the layout
direction = farea.direction = direction

# <-> (Enum('leading', 'trailing', 'center', 'justify')) : The alignment of a line of items within the layout
align = farea.align = align

# <-> (Range(low=0, value=10)) : The amount of horizontal space to place between items
horizontal_spacing = farea.horizontal_spacing = horizontal_spacing

# <-> (Range(low=0, value=10)) : The amount of vertical space to place between items
vertical_spacing = farea.vertical_spacing = vertical_spacing

# <-> (Coerced(Box, (10, 10, 10, 10))) : The margins to use around the outside of the flow area
margins = farea.margins = margins

# <-> (set_default('ignore')) : A FlowArea expands freely in width and height by default
hug_width = farea.hug_width = hug_width
hug_height = farea.hug_height = hug_height

# <-> (Typed(ProxyFlowArea)) : A reference to the ProxyFlowArea object
proxy = farea.proxy = proxy

# Get the flow item children defined on this area
# -> (List(FlowItem)) :
constr = farea.flow_items()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : FlowItem

from enaml.widgets.api import FlowItem

	FlowItem:
		preferred_size = Bool(True)
		align = Enum('leading', 'trailing', 'center')
		stretch = Range(low=0, value=0)
		ortho_stretch = Range(low=0, value=0)
		proxy = Typed(ProxyFlowItem)
		#
		self.flow_widget()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which can be used as an item in a FlowArea
# << (Widget) :
fitem = FlowItem()

# <-> (Bool(True)) : The preferred size of this flow item
preferred_size = fitem.preferred_size = preferred_size

# <-> (Enum('leading', 'trailing', 'center')) : The alignment of this item in the direction orthogonal to the layout flow
align = fitem.align = align

# <-> (Range(low=0, value=0)) : The stretch factor for this item in the flow direction, relative to other items in the same line
stretch = fitem.stretch = stretch

# <-> (Range(low=0, value=0)) : The stretch factor for this item in the orthogonal direction relative to other items in the layout
ortho_stretch = fitem.ortho_stretch = ortho_stretch

# <-> (Typed(ProxyFlowItem)) : A reference to the ProxyFlowItem object
proxy = fitem.proxy = proxy

# Get the flow widget defined on this flow item
# -> (Container) : The last Container defined on the item is the flow widget
cont = fitem.flow_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : FocusTracker

from enaml.widgets.api import FocusTracker

	FocusTracker:
		focused_widget = Typed(Widget)
		proxy = Typed(ProxyFocusTracker)
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An object which tracks the global application focus widget
# << (ToolkitObject) :
focustrk = FocusTracker()

# <-> (Typed(Widget)) : The application widget with the current input focus
focused_widget = focustrk.focused_widget = focused_widget

# <-> (Typed(ProxyFocusTracker)) : A reference to the ProxyFocusTracker object
proxy = focustrk.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Form

from enaml.widgets.api import Form

	Form:
		midline = ConstraintMember()
		row_spacing = Int(10)
		column_spacing = Int(10)
		#
		layout_constraints => ():
			#Container:
		share_layout = Bool(False)
		padding = Coerced(Box, (10, 10, 10, 10))
		resist_width = set_default('ignore')
		resist_height = set_default('ignore')
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyContainer)
		#
		self.widgets()
		self.visible_widgets()
		self.child_added(child)
		self.child_moved(child)
		self.child_removed(child)
		self.layout_constraints(child)
			#Frame:
		border = Typed(Border)
		proxy = Typed(ProxyFrame)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A Container subclass that arranges its children in two columns
# << (Container) :
form = Form()

# <-> (ConstraintMember()) : The ConstraintVariable giving the midline along which the labels and widgets are aligned
midline = form.midline = midline

# <-> (Int(10)) : The spacing to place between the form rows, in pixels
row_spacing = form.row_spacing = row_spacing

# <-> (Int(10)) : The spacing to place between the form columns, in pixels
column_spacing = form.column_spacing = column_spacing

# Get the layout constraints for a Form
# -> (List(constraints)) :
constrs = form.layout_constraints()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Border

from enaml.widgets.api import Border

	Border:
		style = Enum('box', 'panel', 'styled_panel')
		line_style = Enum('plain', 'sunken', 'raised')
		line_width = Range(low=0, value=1)
		midline_width = Range(low=0, value=0)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A class for defining a border on a Frame
# << (Atom) :
brdr = Border()

# <-> (Enum('box', 'panel', 'styled_panel')) : The style of the border
style = brdr.style = style

# <-> (Enum('plain', 'sunken', 'raised')) : The shadow style applied to the border
line_style = brdr.line_style = line_style

# <-> (Range(low=0, value=1)) : The thickness of the outer border line
line_width = brdr.line_width = line_width

# <-> (Range(low=0, value=0)) : The thickness of the inner border line
midline_width = brdr.midline_width = midline_width

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : GroupBox

from enaml.widgets.api import GroupBox

	GroupBox:
		title = Str()
		flat = Bool(False)
		title_align = Enum('left', 'right', 'center')
		proxy = Typed(ProxyGroupBox)
			#Container:
		share_layout = Bool(False)
		padding = Coerced(Box, (10, 10, 10, 10))
		resist_width = set_default('ignore')
		resist_height = set_default('ignore')
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyContainer)
		#
		self.widgets()
		self.visible_widgets()
		self.child_added(child)
		self.child_moved(child)
		self.child_removed(child)
		self.layout_constraints(child)
			#Frame:
		border = Typed(Border)
		proxy = Typed(ProxyFrame)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# The GroupBox container, which introduces a group of widgets with a title and usually has a border
# << (Container) :
grpbox = GroupBox()

# <-> (Str()) : The title displayed at the top of the box
title = grpbox.title = title

# <-> (Bool(False)) :
#		True : displayed with just the title and a header line
#		False : with a full border
flat = grpbox.flat = flat

# <-> (Enum('left', 'right', 'center')) : The alignment of the title text
title_align = grpbox.title_align = title_align

# <-> (Typed(ProxyGroupBox)) : A reference to the ProxyGroupBox object
proxy = grpbox.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : HGroup

from enaml.widgets.api import HGroup

	HGroup:
		spacing = Int(10)
		leading_spacer = Typed(Spacer)
		trailing_spacer = Typed(Spacer)
		align_widths = Bool(True)
		#
		layout_constraints => ():
			#Container:
		share_layout = Bool(False)
		padding = Coerced(Box, (10, 10, 10, 10))
		resist_width = set_default('ignore')
		resist_height = set_default('ignore')
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyContainer)
		#
		self.widgets()
		self.visible_widgets()
		self.child_added(child)
		self.child_moved(child)
		self.child_removed(child)
		self.layout_constraints(child)
			#Frame:
		border = Typed(Border)
		proxy = Typed(ProxyFrame)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A Container subclass which groups child widgets horizontally
# << (Container) :
hgroup = HGroup()

# <-> (Int(10)) : The horizontal spacing to place between widgets
spacing = hgroup.spacing = spacing

# <-> (Typed(Spacer)) : The optional spacer to add as the first layout item
leading_spacer = hgroup.leading_spacer = leading_spacer

# <-> (Typed(Spacer)) : The optional spacer to add as the last layout item
trailing_spacer = hgroup.trailing_spacer = trailing_spacer

# <-> (Bool(True)) : Whether to align the widths of the widgets
align_widths = hgroup.align_widths = align_widths

# The constraints generation for a HGroup
# -> (List(constraints)) :
constrs = hgroup.layout_constraints()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Html

from enaml.widgets.api import Html

	Html:
		source = Str()
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyHtml)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An extremely simple widget for displaying HTML
# << (Control) :
html = Html()

# <-> (Str()) : The Html source code to be rendered
source = html.source = source

# <-> (set_default('ignore')) : An html control expands freely in height and width by default
hug_width = html.hug_width = hug_width
hug_height = html.hug_height = hug_height

# <-> (Typed(ProxyHtml)) : A reference to the ProxyHtml object
proxy = html.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ImageView

from enaml.widgets.api import ImageView

	ImageView:
		image = Typed(Image)
		scale_to_fit = Bool(False)
		allow_upscaling = Bool(True)
		preserve_aspect_ratio = Bool(True)
		hug_width = set_default('weak')
		hug_height = set_default('weak')
		proxy = Typed(ProxyImageView)
		#
		layout_constraints => ():
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which can display an Image with optional scaling
# << (Control) :
imgview = ImageView()

# <-> (Typed(Image)) : The image to display in the viewer
image = imgview.image = image

# <-> (Bool(False)) : Whether or not to scale the image with the size of the component
scale_to_fit = imgview.scale_to_fit = scale_to_fit

# <-> (Bool(True)) : Whether to allow upscaling of an image if scale_to_fit is True
allow_upscaling = imgview.allow_upscaling = allow_upscaling

# <-> (Bool(True)) : Whether or not to preserve the aspect ratio if scaling the image
preserve_aspect_ratio = imgview.preserve_aspect_ratio = preserve_aspect_ratio

# <-> (set_default('weak')) : An image view hugs its width weakly by default
hug_width = imgview.hug_width = hug_width

# <-> (set_default('weak')) : An image view hugs its height weakly by default
hug_height = imgview.hug_height = hug_height

# <-> (Typed(ProxyImageView)) : A reference to the ProxyImageView object
proxy = imgview.proxy = proxy

# Add constraints to preserve the aspect ratio
# -> (constraints) :
constr = imgview.layout_constraints()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : IPythonConsole

from enaml.widgets.api import IPythonConsole

	IPythonConsole:
		initial_ns = Dict()
		exit_requested :: Event()
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyIPythonConsole)
		#
		self.get_var(name, default=None)
		self.update_ns(**kwargs)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which hosts an embedded IPython console
# << (Control) :
ipycli = IPythonConsole()

# <-> (Dict()) : The initial namespace to apply to the console
initial_ns = ipycli.initial_ns = initial_ns

# <-> (Event()) : An event fired when the user invokes a console exit command
exit_requested = ipycli.exit_requested = exit_requested

# <-> (set_default('ignore')) : The ipython console expands freely by default
hug_width = ipycli.hug_width = hug_width
hug_height = ipycli.hug_height = hug_height

# <-> (Typed(ProxyIPythonConsole)) : A reference to the ProxyIPythonConsole object
proxy = ipycli.proxy = proxy

# Get a variable from the console namespace
#	name (Str()) : The name of the variable to retrieve
#	default (object, optional) : The value to return if the variable does not exist
# -> (object) : The variable in the namespace, or the provided default
obj = ipycli.get_var(name, default=None)

# Update the variables in the console namespace
#	kwargs () : The variables to update in the console namespace
ipycli.update_ns(**kwargs)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Label

from enaml.widgets.api import Label

	Label:
		text = Str()
		align = Enum('left', 'right', 'center', 'justify')
		vertical_align = Enum('center', 'top', 'bottom')
		link_activated :: Event()
		hug_width = set_default('weak')
		proxy = Typed(ProxyLabel)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A simple control for displaying read-only text
# << (Control) :
label = Label()

# <-> (Str()) : The unicode text for the label
text = label.text = text

# <-> (Enum('left', 'right', 'center', 'justify')) : The horizontal alignment of the text in the widget area
align = label.align = align

# <-> (Enum('center', 'top', 'bottom')) : The vertical alignment of the text in the widget area
vertical_align = label.vertical_align = vertical_align

# <-> (Event()) : An event emitted when the user clicks a link in the label
link_activated = label.link_activated = link_activated

# <-> (set_default('weak')) : Labels hug their width weakly by default
hug_width = label.hug_width = hug_width

# <-> (Typed(ProxyLabel)) : A reference to the ProxyLabel object
proxy = label.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : MainWindow

from enaml.widgets.api import MainWindow

	MainWindow:
		proxy = Typed(ProxyMainWindow)
		#
		self.menu_bar()
		self.dock_panes()
		self.status_bar()
		self.tool_bars()
			#Window:
		windows = set()
		title = Str()
		initial_position = Coerced(Pos, (-1, -1))
		initial_size = Coerced(Size, (-1, -1))
		modality = Enum('non_modal', 'application_modal', 'window_modal')
		destroy_on_close = Bool(True)
		icon = Typed(Icon)
		always_on_top = Bool(False)
		closing :: Event(CloseEvent)
		closed :: Event()
		visible = set_default(False)
		proxy = Typed(ProxyWindow)
		#
		self.initialize()
		self.destroy()
		self.central_widget()
		self.position()
		self.set_position(pos)
		self.size()
		self.set_size(size)
		self.geometry()
		self.set_geometry(rect)
		self.frame_geometry()
		self.maximize()
		self.is_maximized()
		self.minimize()
		self.is_minimized()
		self.restore()
		self.send_to_front()
		self.send_to_back()
		self.activate_window()
		self.center_on_screen()
		self.center_on_widget(other)
		self.close()
		self.show()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A top level main window widget
# << (Window) :
mainwnd = MainWindow()

# <-> (Typed(ProxyMainWindow)) : A reference to the ProxyMainWindow object
proxy = mainwnd.proxy = proxy

# Get the menu bar defined as a child on the window
# -> (MenuBar) :
mbar = mainwnd.menu_bar()

# Get the dock panes defined as children on the window
# -> (List(DockPane)) :
dockpanes = mainwnd.dock_panes()

# Get the status bar defined as a child on the window
# -> (StatusBar) :
statbar = mainwnd.status_bar()

# Get the tool bars defined as children on the window
# -> (List(tool_bars)) :
toolbars = mainwnd.tool_bars()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : MdiArea

from enaml.widgets.api import MdiArea

	MdiArea:
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		resist_width = set_default('weak')
		resist_height = set_default('weak')
		proxy = Typed(ProxyMdiArea)
		#
		self.mdi_windows()
		self.tile_mdi_windows()
		self.cascade_mdi_windows()
		self.child_added(child)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which acts as a virtual window manager for other top level widget
# << (ConstraintsWidget) :
mdiarea = MdiArea()

# <-> (set_default('ignore')) : An MdiArea expands freely in width and height by default
hug_width = mdiarea.hug_width = hug_width
hug_height = mdiarea.hug_height = hug_height

# <-> (set_default('weak')) : An MdiArea resists clipping only weakly by default
resist_width = mdiarea.resist_width = resist_width
resist_height = mdiarea.resist_height = resist_height

# <-> (Typed(ProxyMdiArea)) : A reference to the ProxyMdiArea object
proxy = mdiarea.proxy = proxy

# Get the mdi windows defined for the area
# -> (List(MdiWindow)) :
mdiwnds = mdiarea.mdi_windows()

# Tile the mdi windows of this area
mdiarea.tile_mdi_windows()

# Cascade the mdi windows of this area
mdiarea.cascade_mdi_windows()

# Ensure that added children are visible if they are supposed to
#	child () :
mdiarea.child_added(child)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : MdiWindow

from enaml.widgets.api import MdiWindow

	MdiWindow:
		title = Str()
		icon = Typed(Icon)
		#
		self.mdi_widget()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which can be used as a window in an MdiArea
# << (Widget) :
mdiwnd = MdiWindow()

# <-> (Str()) : The titlebar text
title = mdiwnd.title = title

# <-> (Typed(Icon)) : The title bar icon
icon = mdiwnd.icon = icon

# Get the mdi widget defined for the window
# -> (Widget) : The last Widget child is the mdi widget
text = mdiwnd.mdi_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Menu

from enaml.widgets.api import Menu

	Menu:
		title = Str()
		enabled = Bool(True)
		visible = Bool(True)
		context_menu = Bool(False)
		proxy = Typed(ProxyMenuBar)
		#
		self.items()
		self.popup()
		self.close()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget used as a menu in a MenuBar
# << (ToolkitObject) :
menu = Menu()

# <-> (Str()) : The title to use for the menu
title = menu.title = title

# <-> (Bool(True)) : Whether or not the menu is enabled
enabled = menu.enabled = enabled

# <-> (Bool(True)) : Whether or not the menu is visible
visible = menu.visible = visible

# <-> (Bool(False)) : Whether this menu should behave as a context menu for its parent
context_menu = menu.context_menu = context_menu

# <-> (Typed(ProxyMenuBar)) : A reference to the ProxyMenuBar object
proxy = menu.proxy = proxy

# Get the items defined on the Menu
# -> (List(Action, ActionGroup, Menu)) :
menus = menu.items()

# Popup the menu over the current mouse location
menu.popup()

# Close the menu
menu.close()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : MenuBar

from enaml.widgets.api import MenuBar

	MenuBar:
		proxy = Typed(ProxyMenuBar)
		#
		self.menus()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget used as a menu bar in a MainWindow
# << (ToolkitObject) :
mbar = MenuBar()

# <-> (Typed(ProxyMenuBar)) : A reference to the ProxyMenuBar object
proxy = mbar.proxy = proxy

# Get the menus defined as children on the menu bar
# -> (List(Menu)) :
menus = mbar.menus()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : MPLCanvas

from enaml.widgets.api import MPLCanvas

	MPLCanvas:
		figure = ForwardTyped(Figure)
		toolbar_visible = Bool(False)
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyMPLCanvas)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A control which can be used to embded a matplotlib figure
# << (Control) :
mplcanv = MPLCanvas()

# <-> (ForwardTyped(Figure)) : The matplotlib figure to display in the widget
figure = mplcanv.figure = figure

# <-> (Bool(False)) : Whether or not the matplotlib figure toolbar is visible
toolbar_visible = mplcanv.toolbar_visible = toolbar_visible

# <-> (set_default('ignore')) : Matplotlib figures expand freely in height and width by default
hug_width = mplcanv.hug_width = hug_width
hug_height = mplcanv.hug_height = hug_height

# <-> (Typed(ProxyMPLCanvas)) : A reference to the ProxyMPLCanvas object
proxy = mplcanv.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : MultilineField

from enaml.widgets.api import MultilineField

	MultilineField:
		text = Str()
		read_only = Bool(False)
		auto_sync_text = Bool(True)
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyMultilineField)
		#
		self.sync_text()
		self.field_text()
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A simple multiline editable text widget
# << (Control) :
mlfield = MultilineField()

# <-> (Str()) : The unicode text to display in the field
text = mlfield.text = text

# <-> (Bool(False)) : Whether or not the field is read only
read_only = mlfield.read_only = read_only

# <-> (Bool(True)) : Whether the text in the control should be auto-synchronized with the text attribute on the field
auto_sync_text = mlfield.auto_sync_text = auto_sync_text

# <-> (set_default('ignore')) : Multiline fields expand freely in width and height by default
hug_width = mlfield.hug_width = hug_width
hug_height = mlfield.hug_height = hug_height

# <-> (Typed(ProxyMultilineField)) : A reference to the ProxyMultilineField object
proxy = mlfield.proxy = proxy

# Synchronize the text with the text in the control
mlfield.sync_text()

# Get the text stored in the field control
# -> (Str()) : The unicode text stored in the field (may be different than that stored in the 'text' attribute)
text = mlfield.field_text()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Notebook

from enaml.widgets.api import Notebook

	Notebook:
		tab_style = Enum('document', 'preferences')
		tab_position = Enum('top', 'bottom', 'left', 'right')
		tabs_closable = Bool(True)
		tabs_movable = Bool(True)
		selected_tab = Str()
		size_hint_mode = Enum('union', 'current')
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyNotebook)
		#
		self.pages()
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A component which displays its children as tabbed pages
# << (ConstraintsWidget) :
noteb = Notebook()

# <-> (Enum('document', 'preferences')) : The style of tabs to use in the notebook
tab_style = noteb.tab_style = tab_style

# <-> (Enum('top', 'bottom', 'left', 'right')) : The position of tabs in the notebook
tab_position = noteb.tab_position = tab_position

# <-> (Bool(True)) : Whether or not the tabs in the notebook should be closable
tabs_closable = noteb.tabs_closable = tabs_closable

# <-> (Bool(True)) : Whether or not the tabs in the notebook should be movable
tabs_movable = noteb.tabs_movable = tabs_movable

# <-> (Str()) : The object name for the selected tab in the notebook
selected_tab = noteb.selected_tab = selected_tab

# <-> (Enum('union', 'current')) : The size hint mode for the stack
size_hint_mode = noteb.size_hint_mode = size_hint_mode

# <-> (set_default('ignore')) : A notebook expands freely in height and width by default
hug_width = noteb.hug_width = hug_width
hug_height = noteb.hug_height = hug_height

# <-> (Typed(ProxyNotebook)) : A reference to the ProxyNotebook object
proxy = noteb.proxy = proxy

# Get the Page children defined on the notebook
# -> (List(Page)) :
pages = noteb.pages()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ObjectCombo

from enaml.widgets.api import ObjectCombo

	ObjectCombo:
		items = List()
		selected = Str()
		to_string = Callable(str)
		to_icon = Callable(lambda item: None)
		editable = Bool(False)
		hug_width = set_default('weak')
		proxy = Typed(ProxyObjectCombo)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A drop-down list from which one item can be selected at a time
# << (Control) :
objcombo = ObjectCombo()

# <-> (List()) : The list of items to display in the combo box
items = objcombo.items = items

# <-> (Str()) : The selected item from the list of items
selected = objcombo.selected = selected

# <-> (Callable(str)) : The callable to use to convert the items into strings for display
to_string = objcombo.to_string = to_string

# <-> (Callable(lambda item: None)) : The callable to use to convert the items into icons for display
to_icon = objcombo.to_icon = to_icon

# <-> (Bool(False)) : Whether the text in the combo box can be edited by the user
editable = objcombo.editable = editable

# <-> (set_default('weak')) : A combo box hugs its width weakly by default
hug_width = objcombo.hug_width = hug_width

# <-> (Typed(ProxyObjectCombo)) : A reference to the ProxyObjectCombo object
proxy = objcombo.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Page

from enaml.widgets.api import Page

	Page:
		title = Str()
		icon = Typed(Icon)
		closable = Bool(True)
		closed :: Event()
		proxy = Typed(ProxyPage)
		#
		self.page_widget()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which can be used as a page in a Notebook control
# << (Widget) :
page = Page()

# <-> (Str()) : The title to use for the page in the notebook
title = page.title = title

# <-> (Typed(Icon)) : The icon to use for the page tab
icon = page.icon = icon

# <-> (Bool(True)) : Whether or not this individual page is closable
closable = page.closable = closable

# <-> (Event()) : An event fired when the user closes the page by clicking on the tab's close button
closed = page.closed = closed

# <-> (Typed(ProxyPage)) : A reference to the ProxyPage object
proxy = page.proxy = proxy

# Get the page widget defined for the page
# -> (Container) : The last child Container is the page widget
cont = page.page_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : PopupView

from enaml.widgets.api import PopupView

	PopupView:
		popup_views = List()
		window_type = Enum('popup', 'tool_tip', 'window')
		anchor_mode = Enum('parent', 'cursor')
		parent_anchor = Coerced(PosF, (0.5, 0.5), coercer=coerce_posf)
		anchor = Coerced(PosF, (0.5, 0.0), coercer=coerce_posf)
		offset = Coerced(Pos, (0, 0), coercer=coerce_pos)
		arrow_edge = Enum('top', 'bottom', 'left', 'right')
		arrow_size = Int(0)
		timeout = Float(0.0)
		fade_in_duration = Int(100)
		fade_out_duration = Int(100)
		close_on_click = Bool(True)
		translucent_background = Bool(True)
		closed :: Event()
		visible = set_default(False)
		proxy = Typed(ProxyPopupView)
		#
		self.central_widget()
		self.show()
		self.close()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which implements a nice popup view
# << (Widget) :
popup = PopupView()

# <-> (List()) : Static class-level storage for the view instances
popup_views = popup.popup_views = popup_views

# <-> (Enum('popup', 'tool_tip', 'window')) : The type of the window to create
window_type = popup.window_type = window_type

# <-> (Enum('parent', 'cursor')) : The mode to use for anchoring
anchor_mode = popup.anchor_mode = anchor_mode

# <-> (Coerced(PosF, (0.5, 0.5), coercer=coerce_posf)) : The relative position on the parent to use as the anchor
parent_anchor = popup.parent_anchor = parent_anchor

# <-> (Coerced(PosF, (0.5, 0.0), coercer=coerce_posf)) : The relative position on the view to use as the view anchor
anchor = popup.anchor = anchor

# <-> (Coerced(Pos, (0, 0), coercer=coerce_pos)) : The offset to apply between the two anchors, in pixels
offset = popup.offset = offset

# <-> (Enum('top', 'bottom', 'left', 'right')) : The edge of the popup view to use for rendering the arrow
arrow_edge = popup.arrow_edge = arrow_edge

# <-> (Int(0)) : The size of the arrow in pixels
arrow_size = popup.arrow_size = arrow_size

# <-> (Float(0.0)) : The timeout, in seconds, before automatically closing the popup
timeout = popup.timeout = timeout

# <-> (Int(100)) : The duration of the fade-in, in milliseconds
fade_in_duration = popup.fade_in_duration = fade_in_duration

# <-> (Int(100)) : The duration of the fade-out, in milliseconds
fade_out_duration = popup.fade_out_duration = fade_out_duration

# <-> (Bool(True)) : Whether or not close the popup view on a mouse click
close_on_click = popup.close_on_click = close_on_click

# <-> (Bool(True)) : Whether or not the background of the popup view is translucent
translucent_background = popup.translucent_background = translucent_background

# <-> (Event()) : An event emitted when the view is closed
closed = popup.closed = closed

# <-> (set_default(False)) : PopupViews are invisible by default
visible = popup.visible = visible

# <-> (Typed(ProxyPopupView)) : A reference to the ProxyPopupView object
proxy = popup.proxy = proxy

# Get the central widget defined on the PopupView
# -> (Container) : The last `Container` child of the window is the central widget
cont = popup.central_widget()

# Show the PopupView
popup.show()

# Close the PopupView
popup.close()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ProgressBar

from enaml.widgets.api import ProgressBar

	ProgressBar:
		minimum = Int(0)
		maximum = Int(100)
		value = Int(0)
		percentage = Property(cached=True)
		text_visible = Bool(False)
		hug_width = set_default('ignore')
		proxy = Typed(ProxyProgressBar)
		#
		self.get_percentage()
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A control which displays a value as a ticking progress bar
# << (Control) :
progbar = ProgressBar()

# <-> (Int(0)) : The minimum progress value
minimum = progbar.minimum = minimum

# <-> (Int(100)) : The maximum progress value
maximum = progbar.maximum = maximum

# <-> (Int(0)) : The position value of the Slider
value = progbar.value = value

# <-> (Property(cached=True)) : A read only cached property which computes the integer percentage
percentage = progbar.percentage = percentage

# <-> (Bool(False)) : Whether or not to display progress percentage on the control
text_visible = progbar.text_visible = text_visible

# <-> (set_default('ignore')) : How strongly a component hugs it's content
hug_width = progbar.hug_width = hug_width

# <-> (Typed(ProxyProgressBar)) : A reference to the ProxyProgressBar object
proxy = progbar.proxy = proxy

# The getter function for the read only percentage property
# -> (int) : Maximum is 99
percent = progbar.get_percentage()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : PushButton

from enaml.widgets.api import PushButton

	PushButton:
		default = Bool(False)
		proxy = Typed(ProxyPushButton)
		#
		self.menu()
			#AbstractButton:
		text = Str()
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		group = ForwardTyped(ButtonGroup)
		checkable = Bool(False)
		checked = Bool(False)
		clicked :: Event(bool)
		toggled :: Event(bool)
		hug_width = set_default('weak')
		proxy = Typed(ProxyAbstractButton)
		#
		self.__init__(parent=None, **kwargs)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A button control represented by a standard push button widget
# << (AbstractButton) :
pushbtn = PushButton()

# <-> (Bool(False)) : Whether this button is the default action button in a dialog
default = pushbtn.default = default

# <-> (Typed(ProxyPushButton)) : A reference to the ProxyPushButton object
proxy = pushbtn.proxy = proxy

# Get the menu defined for the PushButton, if any
# -> (Menu) :
menu = pushbtn.menu()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : RadioButton

from enaml.widgets.api import RadioButton

	RadioButton:
		checkable = set_default(True)
		proxy = Typed(ProxyRadioButton)
			#AbstractButton:
		text = Str()
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		group = ForwardTyped(ButtonGroup)
		checkable = Bool(False)
		checked = Bool(False)
		clicked :: Event(bool)
		toggled :: Event(bool)
		hug_width = set_default('weak')
		proxy = Typed(ProxyAbstractButton)
		#
		self.__init__(parent=None, **kwargs)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An exclusive checkable button represented by a standard radio button widget
# << (AbstractButton) :
radiobtn = RadioButton()

# <-> (set_default(True)) : Radio buttons are checkable by default
checkable = radiobtn.checkable = checkable

# <-> (Typed(ProxyRadioButton)) : A reference to the ProxyRadioButton object
proxy = radiobtn.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : RawWidget

from enaml.widgets.api import RawWidget

	RawWidget:
		proxy = Typed(ProxyRawWidget)
		#
		self.create_widget(parent)
		self.get_widget()
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A raw toolkit-specific control
# << (Control) :
rwidget = RawWidget()

# <-> (Typed(ProxyRawWidget)) : A reference to the proxy Control object (***)
proxy = rwidget.proxy = proxy

# Create the toolkit widget for the control
#	parent (toolkit widget or None) : The parent toolkit widget for the control
# -> (toolkit widget) : The toolkit specific widget for the control
toolkwidget = rwidget.create_widget(parent)

# Retrieve the toolkit widget for the control
# -> (toolkit widget or None) : The scroll widget is the last Container child
toolkwidget = rwidget.get_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ScrollArea

from enaml.widgets.api import ScrollArea

	ScrollArea:
		horizontal_policy = Enum('as_needed', 'always_on', 'always_off')
		vertical_policy = Enum('as_needed', 'always_on', 'always_off')
		widget_resizable = Bool(True)
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyScrollArea)
		#
		self.scroll_widget()
			#Frame:
		border = Typed(Border)
		proxy = Typed(ProxyFrame)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A Frame which displays a single child in a scrollable area
# << (Frame) :
sarea = ScrollArea()

# <-> (Enum('as_needed', 'always_on', 'always_off')) : The horizontal scrollbar policy
horizontal_policy = sarea.horizontal_policy = horizontal_policy

# <-> (Enum('as_needed', 'always_on', 'always_off')) : The vertical scrollbar policy
vertical_policy = sarea.vertical_policy = vertical_policy

# <-> (Bool(True)) : Whether to resize the scroll widget when possible to avoid the need for scrollbars or to make use of extra space
widget_resizable = sarea.widget_resizable = widget_resizable

# <-> (set_default('ignore')) : A scroll area is free to expand in width and height by default
hug_width = sarea.hug_width = hug_width
hug_height = sarea.hug_height = hug_height

# <-> (Typed(ProxyScrollArea)) : A reference to the ProxyScrollArea object
proxy = sarea.proxy = proxy

# Get the scroll widget child defined on the area
# -> (Container) : The scroll widget is the last Container child
cont = sarea.scroll_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Separator

from enaml.widgets.api import Separator

	Separator:
		orientation = Enum('horizontal', 'vertical')
		line_style = Enum('sunken', 'raised', 'plain')
		line_width = Range(low=0, high=3, value=1)
		midline_width = Range(low=0, high=3, value=0)
		auto_hug = Bool(True)
		proxy = Typed(ProxySeparator)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which draws a horizontal or vertical separator line
# << (Control) :
sep = Separator()

# <-> (Enum('horizontal', 'vertical')) : The orientation of the separator line
orientation = sep.orientation = orientation

# <-> (Enum('sunken', 'raised', 'plain')) : The line style for the separator
line_style = sep.line_style = line_style

# <-> (Range(low=0, high=3, value=1)) : The thickness of the outer separator line
line_width = sep.line_width = line_width

# <-> (Range(low=0, high=3, value=0)) : The thickness of the inner separator line
midline_width = sep.midline_width = midline_width

# <-> (Bool(True)) : Whether or not to automatically adjust the 'hug_width' and 'hug_height' values based on the value of 'orientation'
auto_hug = sep.auto_hug = auto_hug

# <-> (Typed(ProxySeparator)) : A reference to the ProxySeparator object
proxy = sep.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Slider

from enaml.widgets.api import Slider

	Slider:
		minimum = Int(0)
		maximum = Int(100)
		value = Int(0)
		single_step = Range(low=1)
		page_step = Range(low=1, value=10)
		tick_position = TickPosition('bottom')
		tick_interval = Range(low=0)
		orientation = Enum('horizontal', 'vertical')
		tracking = Bool(True)
		auto_hug = Bool(True)
		proxy = Typed(ProxySlider)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A simple slider widget that can be used to select from a range of integral values
# << (Control) :
slid = Slider()

# <-> (Int(0)) : The minimum slider value
minimum = slid.minimum = minimum

# <-> (Int(100)) : The maximum slider value
maximum = slid.maximum = maximum

# <-> (Int(0)) : The position value of the Slider
value = slid.value = value

# <-> (Range(low=1)) : Defines the number of steps that the slider will move when the user presses the arrow keys
single_step = slid.single_step = single_step

# <-> (Range(low=1, value=10)) : Defines the number of steps that the slider will move when the user presses the page_up/page_down keys
page_step = slid.page_step = page_step

# <-> (TickPosition('bottom')) : A TickPosition enum value indicating how to display the tick marks
tick_position = slid.tick_position = tick_position

# <-> (Range(low=0)) : The interval to place between slider tick marks in units of value (as opposed to pixels)
tick_interval = slid.tick_interval = tick_interval

# <-> (Enum('horizontal', 'vertical')) : The orientation of the slider
orientation = slid.orientation = orientation

# <-> (Bool(True)) :
#		True : the value is updated while sliding
#		False : it is only updated when the slider is released
tracking = slid.tracking = tracking

# <-> (Bool(True)) : Whether or not to automatically adjust the 'hug_width' and 'hug_height' values based on the value of 'orientation'
auto_hug = slid.auto_hug = auto_hug

# <-> (Typed(ProxySlider)) : A reference to the ProxySlider object
proxy = slid.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : SpinBox

from enaml.widgets.api import SpinBox

	SpinBox:
		minimum = Int(0)
		maximum = Int(100)
		value = Int(0)
		prefix = Str()
		suffix = Str()
		special_value_text = Str()
		single_step = Range(low=1)
		read_only = Bool(False)
		wrapping = Bool(False)
		hug_width = set_default('ignore')
		proxy = Typed(ProxySpinBox)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A spin box widget which manipulates integer values
# << (Control) :
spinbox = SpinBox()

# <-> (Int(0)) : The minimum value for the spin box
minimum = spinbox.minimum = minimum

# <-> (Int(100)) : The maximum value for the spin box
maximum = spinbox.maximum = maximum

# <-> (Int(0)) : The position value of the spin box
value = spinbox.value = value

# <-> (Str()) : An optional prefix to include in the displayed text
prefix = spinbox.prefix = prefix

# <-> (Str()) : An optional suffix to include in the displayed text
suffix = spinbox.suffix = suffix

# <-> (Str()) : Optional text to display when the spin box is at its minimum
special_value_text = spinbox.special_value_text = special_value_text

# <-> (Range(low=1)) : The step size for the spin box
single_step = spinbox.single_step = single_step

# <-> (Bool(False)) : Whether or not the spin box is read-only
#		True : the user will not be able to edit the values in the spin box, but they will still be able to copy the text to the clipboard
#		False :
read_only = spinbox.read_only = read_only

# <-> (Bool(False)) : Whether or not the spin box will wrap around at its extremes
wrapping = spinbox.wrapping = wrapping

# <-> (set_default('ignore')) : A spin box expands freely in width by default
hug_width = spinbox.hug_width = hug_width

# <-> (Typed(ProxySpinBox)) : A reference to the ProxySpinBox object
proxy = spinbox.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : SplitItem

from enaml.widgets.api import SplitItem

	SplitItem:
		stretch = Range(low=0, value=1)
		collapsible = Bool(True)
		proxy = Typed(ProxySplitItem)
		#
		self.split_widget()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which can be used as an item in a Splitter
# << (Widget) :
spltitem = SplitItem()

# <-> (Range(low=0, value=1)) : The stretch factor for this item
stretch = spltitem.stretch = stretch

# <-> (Bool(True)) : Whether or not the item can be collapsed to zero width by the user
collapsible = spltitem.collapsible = collapsible

# <-> (Typed(ProxySplitItem)) : A reference to the ProxySplitItem object
proxy = spltitem.proxy = proxy

# Get the split widget defined on the item
# -> (Container) : The split widget is the last child Container
cont = spltitem.split_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Splitter

from enaml.widgets.api import Splitter

	Splitter:
		orientation = Enum('horizontal', 'vertical')
		live_drag = Bool(True)
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxySplitter)
		#
		self.split_items()
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which displays its children in separate resizable compartments that are connected with a resizing bar
# << (ConstraintsWidget) :
split = Splitter()

# <-> (Enum('horizontal', 'vertical')) : The orientation of the Splitter
#		'horizontal' : children are laid out left to right
#		'vertical' : top to bottom
orientation = split.orientation = orientation

# <-> (Bool(True)) : Whether the child widgets resize as a splitter is being dragged
live_drag = split.live_drag = live_drag

# <-> (set_default('ignore')) : A splitter expands freely in height and width by default
hug_width = split.hug_width = hug_width
hug_height = split.hug_height = hug_height

# <-> (Typed(ProxySplitter)) : A reference to the ProxySplitter object
proxy = split.proxy = proxy

# Get the split item children defined on the splitter
# -> (List(SplitItem)) :
spltitem = split.split_items()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Stack

from enaml.widgets.api import Stack

	Stack:
		index = Int(0)
		transition = Typed(Transition)
		size_hint_mode = Enum('union', 'current')
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyStack)
		#
		self.stack_items()
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A component which displays its children as a stack of widgets, only one of which is visible at a time
# << (ConstraintsWidget) :
stk = Stack()

# <-> (Int(0)) : The index of the visible widget in the stack
index = stk.index = index

# <-> (Typed(Transition)) : The item transition to use when changing between stack items
transition = stk.transition = transition

# <-> (Enum('union', 'current')) :  The size hint mode for the stack
size_hint_mode = stk.size_hint_mode = size_hint_mode

# <-> (set_default('ignore')) : A Stack expands freely in height and width by default
hug_width = stk.hug_width = hug_width
hug_height = stk.hug_height = hug_height

# <-> (Typed(ProxyStack)) : A reference to the ProxyStack widget (***)
proxy = stk.proxy = proxy

# Get the stack items defined on the stack
# -> (List(StackItem)) :
stkitem = stk.stack_items()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Transition

from enaml.widgets.api import Transition

	Transition:
		type = Enum('slide', 'wipe', 'iris', 'fade', 'crossfade')
		direction = Enum('left_to_right', 'right_to_left', 'top_to_bottom', 'bottom_to_top')
		duration = Range(low=0, value=250)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An object representing an animated transition
# << (Atom) :
trans = Transition()

# <-> (Enum('slide', 'wipe', 'iris', 'fade', 'crossfade')) : The type of transition effect to use
type = trans.type = type

# <-> (Enum('left_to_right', 'right_to_left', 'top_to_bottom', 'bottom_to_top')) : The direction of the transition effect
direction = trans.direction = direction

# <-> (Range(low=0, value=250)) : The duration of the transition, in milliseconds
duration = trans.duration = duration

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : StackItem

from enaml.widgets.api import StackItem

	StackItem:
		proxy = Typed(ProxyStackItem)
		#
		self.stack_widget()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which can be used as an item in a Stack
# << (Widget) :
stkitem = StackItem()

# <-> (Typed(ProxyStackItem)) : A reference to the ProxyStackItem object
proxy = stkitem.proxy = proxy

# Get the stack widget defined for the item
# -> (Container) : The stack widget is the last child Container
cont = stkitem.stack_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : StatusBar

from enaml.widgets.api import StatusBar

	StatusBar:
		size_grip_enabled = Bool(True)
		proxy = Typed(ProxyStatusBar)
		#
		self.status_items()
		self.show_message(message, timeout=0)
		self.clear_message()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget used as a status bar in a MainWindow
# << (Widget) :
statbar = StatusBar()

# <-> (Bool(True)) : Whether or not the size grip in the right corner is enabled
size_grip_enabled = statbar.size_grip_enabled = size_grip_enabled

# <-> (Typed(ProxyStatusBar)) : A reference to the ProxyStatusBar object
proxy = statbar.proxy = proxy

# Get the list of status items defined on the status bar
# -> (List(StatusItem)) :
statitem = statbar.status_items()

# Show a temporary message in the status bar
#	message (unicode) : The message to show in the status bar
#	timeout (int, optional) : The number of milliseconds to show the message
statbar.show_message(message, timeout=0)

# Clear any temporary message displayed in the status bar
statitem = statbar.clear_message()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : StatusItem

from enaml.widgets.api import StatusItem

	StatusItem:
		time_format = Enum('normal', 'permanent')
		stretch = Range(low=0)
		proxy = Typed(ProxyStatusItem)
		#
		self.status_widget()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An item which holds a widget to include in a status bar
# << (ToolkitObject) :
statitem = StatusItem()

# <-> (Enum('normal', 'permanent')) : The mode of a status item
#		'normal' : can be obscured by temporary status messages
#		'permanent' : cannot
time_format = statitem.time_format = time_format

# <-> (Range(low=0)) : The stretch factor to apply to this item, relative to the other items in the status bar
stretch = statitem.stretch = stretch

# <-> (Typed(ProxyStatusItem)) : A reference to the ProxyStatusItem object
proxy = statitem.proxy = proxy

# Get the status widget for the item
# -> (Widget) : The last Widget child is used as the status widget
widget = statitem.status_widget()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : TimeSelector

from enaml.widgets.api import TimeSelector

	TimeSelector:
		time_format = Str()
		hug_width = set_default('ignore')
		proxy = Typed(ProxyTimeSelector)
			#BoundedTime:
		minimum = Typed(pytime, args=(0, 0, 0))
		maximum = Typed(pytime, args=(23, 59, 59, 999000))
		time = Typed(pytime, factory=lambda: datetime.now().time())
		proxy = Typed(ProxyBoundedTime)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A time widget that displays a Python datetime.time object using an appropriate toolkit specific control
# << (BoundedTime) :
timesel = TimeSelector()

# <-> (Str()) : A python time format string to format the time
time_format = timesel.time_format = time_format

# <-> (set_default('ignore')) : A time selector is free to expand in width by default
hug_width = timesel.hug_width = hug_width

# <-> (Typed(ProxyTimeSelector)) : A reference to the ProxyDateSelector object
proxy = timesel.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Timer

from enaml.widgets.api import Timer

	Timer:
		interval = Int(0)
		single_shot = Bool(False)
		timeout :: Event()
		proxy = Typed(ProxyTimer)
		#
		self.start()
		self.stop()
		self.is_active()
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# An object which represents a toolkit independent timer
# << (ToolkitObject) :
timer = Timer()

# <-> (Int(0)) : The interval of the timer, in milliseconds
interval = timer.interval = interval

# <-> (Bool(False)) : Whether the timer fires only once, or repeatedly until stopped
single_shot = timer.single_shot = single_shot

# <-> (Event()) : An event fired when the timer times out
timeout = timer.timeout = timeout

# <-> (Typed(ProxyTimer)) : A reference to the ProxyTimer object
proxy = timer.proxy = proxy

# Start or restart the timer
timer.start()

# Stop the timer
timer.stop()

# Returns True if the timer is running, False otherwise
# -> (Bool()) :
#		True : if the timer is running
#		False : otherwise
timer.is_active()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ToolBar

from enaml.widgets.api import ToolBar

	ToolBar:
		button_style = Enum('icon_only', 'text_only', 'text_beside_icon', 'text_under_icon')
		movable = Bool(True)
		floatable = Bool(True)
		floating = Bool(False)
		dock_area = Enum('top', 'right', 'left', 'bottom')
		allowed_dock_areas = List(Enum('top', 'right', 'left', 'bottom', 'all'), ['all'],)
		orientation = Enum('horizontal', 'vertical')
		auto_hug :: Event()
		proxy = Typed(ProxyToolBar)
		#
		self.items()
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which displays a row of tool buttons
# << (ConstraintsWidget) :
toolbar = ToolBar()

# <-> (Enum('icon_only', 'text_only', 'text_beside_icon', 'text_under_icon')) : The button style to apply to actions added to the tool bar
button_style = toolbar.button_style = button_style

# <-> (Bool(True)) : Whether or not the tool bar is movable by the user
movable = toolbar.movable = movable

# <-> (Bool(True)) : Whether or not the tool bar can be floated as a separate window
floatable = toolbar.floatable = floatable

# <-> (Bool(False)) : A boolean indicating whether or not the tool bar is floating
floating = toolbar.floating = floating

# <-> (Enum('top', 'right', 'left', 'bottom')) : The dock area in the MainWindow where the tool bar is docked
dock_area = toolbar.dock_area = dock_area

# <-> (List(Enum('top', 'right', 'left', 'bottom', 'all'), ['all'],)) : The areas in the MainWindow where the tool bar can be docked by the user
allowed_dock_areas = toolbar.allowed_dock_areas = allowed_dock_areas

# <-> (Enum('horizontal', 'vertical')) : The orientation of the toolbar
orientation = toolbar.orientation = orientation

# <-> (Event()) : Whether or not to automatically adjust the 'hug_width' and 'hug_height' values based on the value of 'orientation'
auto_hug = toolbar.auto_hug = auto_hug

# <-> (Typed(ProxyToolBar)) : A reference to the ProxyToolBar object
proxy = toolbar.proxy = proxy

# Get the items defined on the tool bar
# -> (List(Action, ActionGroup)) :
ditems = toolbar.items()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : ToolButton

from enaml.widgets.api import ToolButton

	ToolButton:
		button_style = Enum('icon_only', 'text_only', 'text_beside_icon', 'text_under_icon')
		auto_raise = Bool(True))
		popup_mode = Enum('delayed', 'button', 'instant')
		proxy = Typed(ProxyToolButton)
			#AbstractButton:
		text = Str()
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		group = ForwardTyped(ButtonGroup)
		checkable = Bool(False)
		checked = Bool(False)
		clicked :: Event(bool)
		toggled :: Event(bool)
		hug_width = set_default('weak')
		proxy = Typed(ProxyAbstractButton)
		#
		self.__init__(parent=None, **kwargs)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget for creating tool bar buttons
# << (AbstractButton) :
toolbtn = ToolButton()

# <-> (Enum('icon_only', 'text_only', 'text_beside_icon', 'text_under_icon')) : The button style to apply to this tool button
button_style = toolbtn.button_style = button_style

# <-> (Bool(True))) : Whether or not auto-raise is enabled for the button
auto_raise = toolbtn.auto_raise = auto_raise

# <-> (Enum('delayed', 'button', 'instant')) : The mode for displaying a child popup menu
popup_mode = toolbtn.popup_mode = popup_mode

# <-> (Typed(ProxyToolButton)) : A reference to the ProxyToolButton object
proxy = toolbtn.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : VGroup

from enaml.widgets.api import VGroup

	VGroup:
		spacing = Int(10)
		leading_spacer = Typed(Spacer)
		trailing_spacer = Typed(Spacer)
		#
		layout_constraints => ():
			#Container:
		share_layout = Bool(False)
		padding = Coerced(Box, (10, 10, 10, 10))
		resist_width = set_default('ignore')
		resist_height = set_default('ignore')
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyContainer)
		#
		self.widgets()
		self.visible_widgets()
		self.child_added(child)
		self.child_moved(child)
		self.child_removed(child)
		self.layout_constraints(child)
			#Frame:
		border = Typed(Border)
		proxy = Typed(ProxyFrame)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A Container subclass which groups child widgets vertically
# << (Container) :
vgroup = VGroup()

# <-> (Int(10)) : The vertical spacing to place between widgets
spacing = vgroup.spacing = spacing

# <-> (Typed(Spacer)) : The optional spacer to add as the first layout item
leading_spacer = vgroup.leading_spacer = leading_spacer

# <-> (Typed(Spacer)) : The optional spacer to add as the last layout item
trailing_spacer = vgroup.trailing_spacer = trailing_spacer

# The constraints generation for a VGroup
# -> (List()) :
wnd.layout_constraints()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : VTKCanvas

from enaml.widgets.api import VTKCanvas

	VTKCanvas:
		renderer = vtkRenderer
		renderers = List(vtkRenderer)
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyVTKCanvas)
		#
		self.render()
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A control which can be used to embded vtk renderers
# << (Control) :
vtkcanv = VTKCanvas()

# <-> (vtkRenderer) : The vtk renderer to display in the window
renderer = vtkcanv.renderer = renderer

# <-> (List(vtkRenderer)) : The list of vtk renderers to display in the window
renderers = vtkcanv.renderers = renderers

# <-> (set_default('ignore')) : A web view expands freely in height and width by default
hug_width = vtkcanv.hug_width = hug_width
hug_height = vtkcanv.hug_width = hug_width

# <-> (Typed(ProxyVTKCanvas)) : A reference to the ProxyVTKCanvas object
proxy = vtkcanv.proxy = proxy

# Request a render of the underlying scene
wnd.render()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : WebView

from enaml.widgets.api import WebView

	WebView:
		url = Str()
		html = Str()
		base_url = Str()
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyWebView)
			#Control:
		proxy = Typed(ProxyControl)
			#ConstraintsWidget:
		hug_width = PolicyEnum('strong')
		hug_height = PolicyEnum('strong')
		resist_width = PolicyEnum('strong')
		resist_height = PolicyEnum('strong')
		limit_width = PolicyEnum('ignore')
		limit_height = PolicyEnum('ignore')
		proxy = Typed(ProxyConstraintsWidget)
		#
		self.request_relayout()
		self.when(switch)
		layout_constraints => ():
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A widget which displays a web page
# << (Control) :
webv = WebView()

# <-> (Str()) : The URL to load in the web view
url = webv.url = url

# <-> (Str()) : The html to load into the web view
html = webv.html = html

# <-> (Str()) : The base url for loading content in statically supplied 'html'
base_url = webv.base_url = base_url

# <-> (set_default('ignore')) : A web view expands freely in height and width by default
hug_width = webv.hug_width = hug_width
hug_height = webv.hug_height = hug_height

# <-> (Typed(ProxyWebView)) : A reference to the ProxyWebView object
proxy = webv.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Feature

from enaml.widgets.api import Feature

	Feature:
			#IntEnum:
# An IntEnum defining the advanced widget features
# << (IntEnum) :
#	FocusTraversal : Enables support for custom focus traversal functions
#	FocusEvents : Enables support for focus events
#	DragEnabled : Enables support for drag operations
#	DropEnabled : Enables support for drop operations
feat = Feature()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Window

from enaml.widgets.api import Window

	Window:
		windows = set()
		title = Str()
		initial_position = Coerced(Pos, (-1, -1))
		initial_size = Coerced(Size, (-1, -1))
		modality = Enum('non_modal', 'application_modal', 'window_modal')
		destroy_on_close = Bool(True)
		icon = Typed(Icon)
		always_on_top = Bool(False)
		closing :: Event(CloseEvent)
		closed :: Event()
		visible = set_default(False)
		proxy = Typed(ProxyWindow)
		#
		self.initialize()
		self.destroy()
		self.central_widget()
		self.position()
		self.set_position(pos)
		self.size()
		self.set_size(size)
		self.geometry()
		self.set_geometry(rect)
		self.frame_geometry()
		self.maximize()
		self.is_maximized()
		self.minimize()
		self.is_minimized()
		self.restore()
		self.send_to_front()
		self.send_to_back()
		self.activate_window()
		self.center_on_screen()
		self.center_on_widget(other)
		self.close()
		self.show()
			#Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

enamldef Main(Window):
	attr data = 0
	attr data: Int() = 0
	Container:
		...

# A top-level Window component
# << (Widget) :
wnd = Window()

# <-> (set()) : A static set of windows being used by the application
windows = wnd.windows = windows

# <-> (Str()) : The titlebar text
title = wnd.title = title

# <-> (Coerced(Pos, (-1, -1))) : The initial position of the window frame
initial_position = wnd.initial_position = initial_position

# <-> (Coerced(Size, (-1, -1))) : The initial size of the window client area
initial_size = wnd.initial_size = initial_size

# <-> (Enum('non_modal', 'application_modal', 'window_modal')) : An enum which indicates the modality of the window
modality = wnd.modality = modality

# <-> (Bool(True)) : Destroy window on the completion of the `closed` event
destroy_on_close = wnd.destroy_on_close = destroy_on_close

# <-> (Typed(Icon)) : The title bar icon
icon = wnd.icon = icon

# <-> (Bool(False)) : Whether the window stays on top of other windows on the desktop
always_on_top = wnd.always_on_top = always_on_top

# <-> (Event(CloseEvent)) : An event fired when the user request the window to be closed
closing = wnd.closing = closing

# <-> (Event()) : An event fired when the window is closed
closed = wnd.closed = closed

# <-> (set_default(False)) : Windows are invisible by default
visible = wnd.visible = visible

# <-> (Typed(ProxyWindow)) : A reference to the ProxyWindow object
proxy = wnd.proxy = proxy

# An overridden initializer method
wnd.initialize()

# An overridden destructor method
wnd.destroy()

# Get the central widget defined on the window
# -> (Container) :
cont = wnd.central_widget()

# Get the position of the window frame
# -> (Pos) : The current position of the window frame
pos = wnd.position()

# Set the position of the window frame
#	pos (Pos) : The desired position of the window the window frame
wnd.set_position(pos)

# Get the size of the window client area
# -> (Size) : The current size of the window client area
size = wnd.size()

# Set the size of the window client area
#	size (Size) : The desired size of the window client area
wnd.set_size(size)

# Get the geometry of the window client area
# -> (Rect) : The current geometry of the window client area
rect = wnd.geometry()

# Set the geometry of the window client area
#	rect (Rect) : The desired geometry of the window client area
wnd.set_geometry(rect)

# Get the geometry of the window frame
# -> (Rect) : The current geometry of the window frame
rect = wnd.frame_geometry()

# Maximize the window
wnd.maximize()

# Get whether the window is maximized
# -> (Bool()) :
ismax = wnd.is_maximized()

# Minimize the window
wnd.minimize()

# Get whether the window is minimized
# -> (Bool()) :
ismin = wnd.is_minimized()

# Restore the window from a maximized or minimized state
wnd.restore()

# Send the window to the top of the Z-order
wnd.send_to_front()

# Send the window to the bottom of the Z-order
wnd.send_to_back()

# Set this window to be the active application window
wnd.activate_window()

# Center the window on the screen
wnd.center_on_screen()

# Center this window on another widget
#	other (Widget) : The widget onto which to center this window
wnd.center_on_widget(other)

# Close the window
wnd.close()

# Show the window to the screen
wnd.show()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Widget : Widget

from enaml.widgets.widget import Widget

	Widget:
		enabled = Bool(True)
		visible = Bool(True)
		background = ColorMember()
		foreground = ColorMember()
		font = FontMember()
		minimum_size = Coerced(Size, (-1, -1))
		maximum_size = Coerced(Size, (-1, -1))
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		proxy = Typed(ProxyWidget)
		#
		self.restyle()
		self.show(s)
		self.hide()
		#
		next_focus_child => (current):
		previous_focus_child => (current):
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
			#ToolkitObject:
		activated :: Event()
		proxy = Typed(ProxyToolkitObject)
		proxy_is_active = flag_property(ACTIVE_PROXY_FLAG)
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
		self.child_removed(child)
		self.activate_proxy()
		self.activate_top_down()
		self.activate_bottom_up()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# The base class of visible widgets in Enaml
# << (ToolkitObject, Stylable) :
wdgt = Widget()

# <-> (Bool(True)) : Whether or not the widget is enabled
enabled = wdgt.enabled = enabled

# <-> (Bool(True)) : Whether or not the widget is visible
visible = wdgt.visible = visible

# <-> (ColorMember()) : The background color of the widget
background = wdgt.background = background

# <-> (ColorMember()) : The foreground color of the widget
foreground = wdgt.foreground = foreground

# <-> (FontMember()) : The font used for the widget
font = wdgt.font = font

# <-> (Coerced(Size, (-1, -1))) : The minimum size for the widget
minimum_size = wdgt.minimum_size = minimum_size

# <-> (Coerced(Size, (-1, -1))) : The maximum size for the widget
maximum_size = wdgt.maximum_size = maximum_size

# <-> (Str()) : The tool tip to show when the user hovers over the widget
tool_tip = wdgt.tool_tip = tool_tip

# <-> (Str()) : The status tip to show when the user hovers over the widget
status_tip = wdgt.status_tip = status_tip

# <-> (Coerced(Feature.Flags)) : Set the extra features to enable for this widget
features = wdgt.features = features

# <-> (ProxyWidget) : A reference to the ProxyWidget object
proxy = wdgt.proxy = proxy

# Ensure the widget is shown
wdgt.show()

# Ensure the widget is hidden
wdgt.hide()

# Set the keyboard input focus to this widget (DON'T)
wdgt.set_focus()

# Clear the keyboard input focus from this widget (DON'T)
wdgt.clear_focus()

# Test whether this widget has input focus (DON'T)
# -> (bool) : True if this widget has input focus, False otherwise
focused = wdgt.has_focus()

# Give focus to the next widget in the focus chain (DON'T)
wdgt.focus_next_child()

# Give focus to the previous widget in the focus chain (DON'T)
wdgt.focus_previous_child()

# Compute the next widget which should gain focus (to be reimplemented)
#	current (Widget or None) :
#		Widget : current widget with input focus
#		None : if no widget has focus or if the toolkit widget with focus does not correspond to an Enaml widget
# -> (Widget or None) :
#		Widget : next widget which should gain focus
#		None : to follow the default toolkit behavior
focused = wdgt.next_focus_child(current)

# Compute the previous widget which should gain focus (to be reimplemented)
#	current (Widget or None) :
#		Widget : current widget with input focus
#		None : if no widget has focus or if the toolkit widget with focus does not correspond to an Enaml widget
# -> (Widget or None) :
#		Widget : next widget which should gain focus
#		None : to follow the default toolkit behavior
focused = wdgt.previous_focus_child(current)

# A method invoked when the widget gains input focus (to be reimplemented)
wdgt.focus_gained()

# A method invoked when the widget loses input focus (to be reimplemented)
wdgt.focus_lost()

# A method called at the start of a drag-drop operation (to be reimplemented)
# -> (DragData) : An Enaml DragData object which holds the drag data
dragged = wdgt.drag_start()

# A method called at the end of a drag-drop operation (to be reimplemented)
#	drag_data (DragData) : The drag data created by the `drag_start` method
#	result (DropAction) : The requested drop action when the drop completed
wdgt.drag_end(drag_data, result)

# A method invoked when a drag operation enters the widget (to be reimplemented)
#	event (DropEvent) : The event representing the drag-drop operation
wdgt.drag_enter(event)

# A method invoked when a drag operation moves in the widget (to be reimplemented)
#	event (DropEvent) : The event representing the drag-drop operation
wdgt.drag_move(event)

# A method invoked when a drag operation leaves the widget (to be reimplemented)
wdgt.drag_leave(event)

# A method invoked when the user drops the data on the widget (to be reimplemented)
#	event (DropEvent) : The event representing the drag-drop operation
wdgt.drop(event)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Workbench : Extension

from enaml.workbench.api import Extension

	Extension:
		id = Str()
		point = Str()
		rank = Int()
		factory = Callable()
		description = Str()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class which represents a plugin extension
#	An Extension must be declared as a child of a PluginManifest
# << (Declarative) :
ext = Extension()

# <-> (Str()) : The globally unique identifier for the extension
id = ext.id = id

# <-> (Str()) : The fully qualified id of the target extension point
point = ext.point = point

# <-> (Int()) : An optional rank to use for order the extension among others
rank = ext.rank = rank

# <-> (Callable()) : A callable which will create the implementation object for the extension point
factory = ext.factory = factory

# <-> (Str()) : An optional description of the extension
description = ext.description = description

# -> (Str()) : Get the plugin id from the parent plugin manifest
plugin_id = ext.plugin_id

# -> (Str()) : Get the fully qualified extension identifer
#	'%s.%s'
qualified_id = ext.qualified_id

# Find a child by the given type
#	kind (type) : The declarative type of the child of interest
#	reverse (bool, optional) : Whether to search in reversed order
# -> (kind or None) : The first child found of the requested type
child = ext.get_child(kind, reverse=False)

# Get all the children of the given type
#	kind (type) : The declarative type of the children of interest
# -> (List(kind)) : The list of children of the request type
children = ext.get_children(kind)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench : ExtensionPoint

from enaml.workbench.api import ExtensionPoint

	ExtensionPoint:
		id = Str()
		extensions = Tuple()
		description = Str()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class which represents a plugin extension point
#	An ExtensionPoint must be declared as a child of a PluginManifest
# << (Declarative) :
extpt = ExtensionPoint()

# <-> (Str()) : The globally unique identifier for the extension point
id = extpt.id = id

# <-> (Tuple()) : The tuple of extensions contributed to this extension point
extensions = extpt.extensions = extensions

# <-> (Str()) : An optional description of the extension point
description = extpt.description = description

# -> (Str()) : Get the plugin id from the parent plugin manifest
plugin_id = extpt.plugin_id

# -> (Str()) : Get the fully qualified extension point identifer
#	'%s.%s'
qualified_id = ext.qualified_id

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench : Plugin

from enaml.workbench.api import Plugin

	Plugin:
		self.workbench
		#
		self.start()
		self.stop()
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A base class for defining workbench plugins
# << (Atom) :
plugin = Plugin()

# -> (Workbench) : Get the workbench which is handling the plugin
workbench = plugin.workbench

# Start the life-cycle of the plugin (to be reimplemented)
plugin.start()

# Stop the life-cycle of the plugin (to be reimplemented)
plugin.stop()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench : PluginManifest

from enaml.workbench.api import PluginManifest

	PluginManifest:
		id = Str()
		factory = Callable(plugin_factory) -> Plugin
		description = Str()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class which represents a plugin manifest
# << (Declarative) :
pluginmf = PluginManifest()

# <-> (Str()) : The globally unique identifier for the plugin
id = pluginmf.id = id

# <-> (Callable(plugin_factory) -> Plugin) : The factory which will create the Plugin instance
factory = pluginmf.factory = factory

# <-> (Str()) : An optional description of the plugin
description = pluginmf.description = description

# -> (List(Extension)) : Get the list of extensions defined by the manifest
extensions = pluginmf.extensions

# -> (List(ExtensionPoint)) : Get the list of extensions points defined by the manifest
extensionpts = pluginmf.extension_points

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench : Workbench

from enaml.workbench.api import Workbench

	Workbench:
		plugin_added :: Event(str)
		plugin_removed :: Event(str)
		extension_point_added :: Event(str)
		extension_point_removed :: Event(str)
		#
		self.register(manifest)
		self.unregister(plugin_id)
		self.get_manifest(plugin_id)
		self.get_plugin(plugin_id, force_create=True)
		self.get_extension_point(extension_point_id)
		self.get_extension_points(self)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A base class for creating plugin-style applications
# << (Atom) :
workb = Workbench()

# <-> (Event(str)) : An event fired when a plugin is added to the workbench
plugin_added = workb.plugin_added = plugin_added

# <-> (Event(str)) : An event fired when a plugin is removed from the workbench
plugin_removed = workb.plugin_removed = plugin_removed

# <-> (Event(str)) : An event fired when an extension point is added to the workbench
extension_point_added = workb.extension_point_added = extension_point_added

# <-> (Event(str)) : An event fired when an extension point is removed from the workbench
extension_point_removed = workb.extension_point_removed = extension_point_removed

# Register a plugin with the workbench
#	manifest (PluginManifest) : The plugin manifest to register with the workbench
workb.register(manifest)

# Remove a plugin from the workbench
#	plugin_id (Str()) : The identifier of the plugin of interest
workb.unregister(plugin_id)

# Get the plugin manifest for a given plugin id
#	plugin_id (Str()) : The identifier of the plugin of interest
# -> (PluginManifest or None) :
#		PluginManifest : The manifest for the plugin of interest
#		None : if it does not exist
plugmanif = workb.get_manifest(plugin_id)

# Get the plugin object for a given plugin id
#	plugin_id (Str()) : The identifier of the plugin of interest
#	force_create (Bool(True)) : Whether to automatically import and start the plugin object if it is not already active
# -> (Plugin or None) :
#		Plugin : The plugin of interest
#		None : if it does not exist and/or could not be created
plugin = workb.get_plugin(plugin_id, force_create=True)

# Get the extension point associated with an id
#	extension_point_id (Str()) : The fully qualified id of the extension point of interest
# -> (ExtensionPoint or None) :
#		ExtensionPoint : The desired ExtensionPoint
#		None : if it does not exist
extpt = workb.get_extension_point(extension_point_id)

# Get all of the extension points in the workbench
# -> (List(ExtensionPoint)) : A list of all of the extension points in the workbench
extpts = workb.get_extension_points()

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Workbench.Core : Command

from enaml.workbench.core.api import Command

	Command:
		id = Str()
		description = Str()
		handler = Callable(ExecutionEvent)
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class for defining a workbench command
# << (Declarative) :
cmd = Command()

# <-> (Str()) : The globally unique identifier for the command
id = cmd.id = id

# <-> (Str()) : An optional description of the command
description = cmd.description = description

# <-> (Callable(ExecutionEvent)) : A required callable which handles the command
handler = cmd.handler = handler

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Workbench.Ui : ActionItem

from enaml.workbench.ui.api import ActionItem

	ActionItem:
		path = Str()
		group = Str()
		before = Str()
		after = Str()
		command = Str()
		parameters = Dict()
		label = Str()
		shortcut = Str()
		visible = Bool(True)
		enabled = Bool(True)
		checkable = Bool(False)
		checked = Bool(False)
		icon = Typed(Icon)
		tool_tip = Str()
		status_tip = Str()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class for defining a workbench action item.
# << (Declarative) :
aitem = ActionItem()

# <-> (Str()) : The "/" separated path to this item in the menu bar
path = aitem.path = path

# <-> (Str()) : The parent menu group to which this action item belongs
group = aitem.group = group

# <-> (Str()) : The action item will appear before this item in its group
before = aitem.before = before

# <-> (Str()) : The action item will appear after this item in its group
after = aitem.after = after

# <-> (Str()) : The id of the Command invoked by the action
command = aitem.command = command

# <-> (Dict()) : The user parameters to pass to the command handler
parameters = aitem.parameters = parameters

# <-> (Str()) : The display label for the action
label = aitem.label = label

# <-> (Str()) : The shortcut keybinding for the action. e.g. Ctrl+C
shortcut = aitem.shortcut = shortcut

# <-> (Bool(True)) : Whether or not the action is visible
visible = aitem.visible = visible

# <-> (Bool(True)) : Whether or not the action is enabled
enabled = aitem.enabled = enabled

# <-> (Bool(False)) : Whether or not the action is checkable
checkable = aitem.checkable = checkable

# <-> (Bool(False)) : Whether or not the checkable action is checked
checked = aitem.checked = checked

# <-> (Typed(Icon)) : The default display icon for the action
icon = aitem.icon = icon

# <-> (Str()) : The tooltip for the action
tool_tip = aitem.tool_tip = tool_tip

# <-> (Str()) : The statustip for the action
status_tip = aitem.status_tip = status_tip

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench.Ui : Autostart

from enaml.workbench.ui.api import Autostart

	Autostart:
		plugin_id = Str()
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative object for use with auto start extensions
# << (Declarative) :
astart = Autostart()

# <-> (Str()) : The id of the plugin which should be preemptively started
plugin_id = astart.plugin_id = plugin_id

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench.Ui : Branding

from enaml.workbench.ui.api import Branding

	Branding:
		title = Str()
		icon = Typed(Icon)
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class for defining window branding
# << (Declarative) :
brand = Branding()

# <-> (Str()) : The primary title of the workbench window
title = brand.title = title

# <-> (Typed(Icon)) : The icon for the workbench window
icon = brand.icon = icon

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench.Ui : ItemGroup

from enaml.workbench.ui.api import ItemGroup

	ItemGroup:
		id = Str()
		visible = Bool(True)
		enabled = Bool(True)
		exclusive = Bool(False)
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class for defining an item group in a menu.
# << (Declarative) :
igroup = ItemGroup()

# <-> (Str()) : The identifier of group within the menu
id = igroup.id = id

# <-> (Bool(True)) : Whether or not the group is visible
visible = igroup.visible = visible

# <-> (Bool(True)) : Whether or not the group is enabled
enabled = igroup.enabled = enabled

# <-> (Bool(False)) : Whether or not checkable ations in the group are exclusive
exclusive = igroup.exclusive = exclusive

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench.Ui : MenuItem

from enaml.workbench.ui.api import MenuItem

	MenuItem:
		path = Str()
		group = Str()
		before = Str()
		after = Str()
		label = Str()
		visible = Bool(True)
		enabled = Bool(True)
		#
		self.item_groups = List(ItemGroup)
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class for defining a menu in the workbench
# << (Declarative) :
mitem = MenuItem()

# <-> (Str()) : The "/" separated path to this item in the menu bar
path = mitem.path = path

# <-> (Str()) : The parent menu group to which this menu item belongs
group = mitem.group = group

# <-> (Str()) : The menu item will appear before this item in its group
before = mitem.before = before

# <-> (Str()) : The menu item will appear after this item in its group
after = mitem.after = after

# <-> (Str()) : The display label for the menu
label = mitem.label = label

# <-> (Bool(True)) : Whether or not the menu is visible
visible = mitem.visible = visible

# <-> (Bool(True)) : Whether or not the menu is enabled
enabled = mitem.enabled = enabled

# <-> (List(ItemGroup)) : Get the item groups defined on this menu item
item_groups = mitem.item_groups

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench.Ui : UIWorkbench

from enaml.workbench.ui.api import UIWorkbench

	UIWorkbench:
		self.run()
			#Workbench:
		plugin_added :: Event(str)
		plugin_removed :: Event(str)
		extension_point_added :: Event(str)
		extension_point_removed :: Event(str)
		#
		self.register(manifest)
		self.unregister(plugin_id)
		self.get_manifest(plugin_id)
		self.get_plugin(plugin_id, force_create=True)
		self.get_extension_point(extension_point_id)
		self.get_extension_points(self)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A class for creating workbench UI applications.
# << (Workbench) :
uiworkb = UIWorkbench()

# Run the UI workbench application
uiworkb.run()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# Workbench.Ui : Workspace

from enaml.workbench.ui.api import Workspace

	Workspace:
		window_title = Str()
		content = Typed(Container)
		workbench = Typed(Workbench)
			#Declarative:
		name = Str()
		initialized :: Event()
		is_initialized = flag_property()
		#
		self.initialize()
		self.destroy()
		self.child_added(child)
			#Object:
		name = Str()
		parent = Object()
		children = List(Object())
		is_destroyed = flag_property(DESTROYED_FLAG)
		destroyed :: Event()
		#
		parent_changed => (old, new):
		child_added => (child):
		child_moved => (child):
		child_removed => (child):
		#
		self.destroy()
		self.set_parent(parent)
		self.insert_children(before, insert)
		self.root_object()
		self.traverse(depth_first=False)
		self.traverse_ancestors(root=None)
		self.find(name, regex=False)
		self.find_all(name, regex=False)
			#Atom:
		self.__init__(**kwargs)
		self.freeze()
		self.get_member(member: str)
		self.has_observer(member: str, func: Callable[[Dict[str, Any]], None])
		self.has_observers(member: str)
		self.notifications_enabled()
		self.notify(member_name: str, *args, **kwargs)
		self.observe(member: str, func: Callable[[Dict[str, Any]], None])
		self.set_notifications_enabled(enabled: bool)
		self.unobserve(member: str, func: Callable[[Dict[str, Any]], None])
		self.__sizeof__()

# A declarative class for defining a workspace object
# << (Declarative) :
workspc = Workspace()

# <-> (Str()) : Extra information to display in the window title bar
window_title = workspc.window_title = window_title

# <-> (Typed(Container)) : The primary window content for the workspace
content = workspc.content = content

# <-> (Typed(Workbench)) : The workbench object which owns the workspace
workbench = workspc.workbench = workbench

# Start the workspace (to be reimplemented)
workspc.start()

# Stop the workspace (to be reimplemented)
workspc.stop()

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
