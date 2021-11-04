#!/usr/bin/env python3
# author: d.koch
# coding: utf-8
# naming: pep-0008
# typing: pep-0484
# docstring: pep-0257
# indentation: tabulation (4 spc)

""" enamlx-api.py
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

#	(atom)			Atom
#	widgets			+--	Brush
#					|		color = ColorMember()
#					|		image = Instance(Image)
#					|		style = Enum('solid', 'dense1', 'dense2', 'dense3', 'dense4', 'dense5', 'dense6', 'dense7', 'horizontal', 'vertical', 'cross', 'diag', 'bdiag', 'fdiag', 'linear', 'radial', 'conical', 'texture', 'none')
#	(enaml)			+--	Object
#	(enaml)			|	+--	Declarative
#	(enaml)			|		+--	ToolkitObject
#	widgets			|			+--	GraphicsItem
#					|			|	|	<GraphicsView
#					|			|	|	proxy = Typed(ProxyGraphicsItem)
#					|			|	|	position = PointMember()
#					|			|	|	rotation = Float(strict=False)
#					|			|	|	scale = Float(1.0, strict=False)
#					|			|	|	opacity = Float(1.0, strict=False)
#					|			|	|	selected = Bool()
#					|			|	|	enabled = Bool(True)
#					|			|	|	visible = Bool(True)
#					|			|	|	tool_tip = Str()
#					|			|	|	status_tip = Str()
#					|			|	|	features = Coerced(Feature.Flags)
#					|			|	|	extra_features = Coerced(GraphicFeature.Flags)
#					|			|	|	request_update = Event()
#					|			|	|	selectable = Bool()
#					|			|	|	movable = Bool()
#					|			|	|	#
#					|			|	|	self.show()
#					|			|	|	self.hide()
#					|			|	|	#
#					|			|	|	focus_gained => ():
#					|			|	|	focus_lost => ():
#					|			|	|	drag_start => ():
#					|			|	|	drag_end => (drag_data, result):
#					|			|	|	drag_enter => (event):
#					|			|	|	drag_move => (event):
#					|			|	|	drag_leave => ():
#					|			|	|	drop => (event):
#					|			|	|	mouse_press_event => (event):
#					|			|	|	mouse_move_event => (event):
#					|			|	|	mouse_release_event => (event):
#					|			|	|	wheel_event => (event):
#					|			|	|	draw => (painter, options, widget):
#					|			|	+--	AbstractGraphicsShapeItem
#					|			|	|	|	proxy = Typed(ProxyAbstractGraphicsShapeItem)
#					|			|	|	|	pen = Instance(Pen)
#					|			|	|	|	brush = Instance(Brush)
#	widgets			|			|	|	+--	GraphicsEllipseItem
#					|			|	|	|		proxy = Typed(ProxyGraphicsEllipseItem)
#					|			|	|	|		width = Float(10.0, strict=False)
#					|			|	|	|		height = Float(10.0, strict=False)
#					|			|	|	|		span_angle = Float(360.0, strict=False)
#					|			|	|	|		start_angle = Float(0.0, strict=False)
#	widgets			|			|	|	+--	GraphicsLineItem
#					|			|	|	|		proxy = Typed(ProxyGraphicsLineItem)
#					|			|	|	|		point = List(PointMember())
#	widgets			|			|	|	+--	GraphicsPathItem
#					|			|	|	|		proxy = Typed(ProxyGraphicsPathItem)
#					|			|	|	|		path = Value()
#	widgets			|			|	|	+--	GraphicsPolygonItem
#					|			|	|	|		proxy = Typed(ProxyGraphicsPolygonItem)
#					|			|	|	|		points = List(PointMember())
#	widgets			|			|	|	+--	GraphicsRectItem
#					|			|	|	|		proxy = Typed(ProxyGraphicsRectItem)
#					|			|	|	|		width = Float(10.0, strict=False)
#					|			|	|	|		height = Float(10.0, strict=False)
#	widgets			|			|	|	+--	GraphicsTextItem
#					|			|	|			proxy = Typed(ProxyGraphicsTextItem)
#					|			|	|			text = Str()
#					|			|	|			font = FontMember()
#	widgets			|			|	+--	GraphicsImageItem
#					|			|	|		proxy = Typed(ProxyGraphicsImageItem)
#					|			|	|		image = Instance(Image)
#	widgets			|			|	+--	GraphicsItemGroup
#					|			|	|		proxy = Typed(ProxyGraphicsItemGroup)
#	widgets			|			|	+--	GraphicsWidget
#					|			|			proxy = Typed(ProxyGraphicsWidget)
#	(enaml)			|			+--	Widget
#	(enaml)			|				+--	ConstraintsWidget
#	(enaml)			|					+--	Control
#					|					|	+--	AbstractItemView
#					|					|	|	|	hug_width = set_default('ignore')
#					|					|	|	|	hug_height = set_default('ignore')
#					|					|	|	|	items = ContainerList(default=[])
#					|					|	|	|	selection_mode = Enum('extended', 'none', 'multi', 'single', 'contiguous')
#					|					|	|	|	selection_behavior = Enum('items', 'rows', 'columns')
#					|					|	|	|	selection = ContainerList(default=[])
#					|					|	|	|	scroll_to_bottom = Bool(False)
#					|					|	|	|	alternating_row_colors = Bool(False)
#					|					|	|	|	cell_padding = Int(0)
#					|					|	|	|	auto_resize = Bool(True)
#					|					|	|	|	resize_mode = Enum('interactive', 'fixed', 'stretch', 'resize_to_contents', 'custom')
#					|					|	|	|	word_wrap = Bool(False)
#					|					|	|	|	show_vertical_header = Bool(True)
#					|					|	|	|	vertical_headers = ContainerList()
#					|					|	|	|	vertical_stretch = Bool(False)
#					|					|	|	|	vertical_minimum_section_size = Int(0)
#					|					|	|	|	show_horizontal_header = Bool(True)
#					|					|	|	|	horizontal_headers << ContainerList()
#					|					|	|	|	horizontal_stretch = Bool(False)
#					|					|	|	|	horizontal_minimum_section_size = Int(0)
#					|					|	|	|	sortable = Bool(True)
#					|					|	|	|	current_row = Int(0)
#					|					|	|	|	current_column = Int(0)
#					|					|	|	|	visible_row = Int(0)
#					|					|	|	|	visible_rows = Int(100)
#					|					|	|	|	visible_column = Int(0)
#					|					|	|	|	visible_columns = Int(1)
#	widgets			|					|	|	+--	TableView
#					|					|	|	|		proxy = Typed(ProxyTableView)
#					|					|	|	|		show_grid = Bool(True)
#	widgets			|					|	|	+--	TreeView
#					|					|	|			proxy = Typed(ProxyTreeView)
#					|					|	|			show_root = Bool(True)
#					|					|	+--	AbstractWidgetItemGroup
#					|					|	|	|	>AbstractWidgetItem
#					|					|	|	|	clicked = d_(Event(), writable=False)
#					|					|	|	|	double_clicked = d_(Event(), writable=False)
#					|					|	|	|	entered = d_(Event(), writable=False)
#					|					|	|	|	pressed = d_(Event(), writable=False)
#					|					|	|	|	selection_changed = d_(Event(bool), writable=False)
#					|					|	|	+--	AbstractWidgetItem
#					|					|	|	|	|	row = d_(Int(), writable=False)
#					|					|	|	|	|	column = d_(Int(), writable=False)
#					|					|	|	|	|	text = d_(Str())
#					|					|	|	|	|	text_alignment = d_(Enum(*[(h, v) for h in ('left', 'right', 'center', 'justify') for v in ('center', 'top', 'bottom')]))
#					|					|	|	|	|	icon = d_(Typed(Icon))
#					|					|	|	|	|	icon_size = d_(Coerced(Size, (-1, -1)))
#					|					|	|	|	|	selectable = d_(Bool(True))
#					|					|	|	|	|	selected = d_(Bool())
#					|					|	|	|	|	checkable = d_(Bool())
#					|					|	|	|	|	checked = d_(Bool())
#					|					|	|	|	|	editable = d_(Bool())
#					|					|	|	|	|	changed = d_(Event(), writable=False)
#					|					|	|	|	|	toggled = d_(Event(bool), writable=False)
#	widgets			|					|	|	|	+--	TableViewItem
#					|					|	|	|	|		proxy = Typed(ProxyTableViewItem)
#	widgets			|					|	|	|	+--	TreeViewItem
#					|					|	|	|	|		<TreeViewItem
#					|					|	|	|	|		>TreeViewItem
#					|					|	|	|	|		proxy = Typed(ProxyTreeViewItem)
#					|					|	|	|	|		items = ContainerList(default=[])
#					|					|	|	|	|		visible_row = Int(0)
#					|					|	|	|	|		visible_rows = Int(100)
#					|					|	|	|	|		visible_column = Int(0)
#					|					|	|	|	|		visible_columns = Int(1)
#	widgets			|					|	|	|	+--	TreeViewColumn
#					|					|	|	|			proxy = Typed(ProxyTreeViewColumn)
#	widgets			|					|	|	+--	TableViewRow
#					|					|	|	|		proxy = Typed(ProxyTableViewRow)
#					|					|	|	|		row = Int()
#	widgets			|					|	|	+--	TableViewColumn
#					|					|	|			proxy = Typed(ProxyTableViewColumn)
#					|					|	|			column = Int()
#	widgets			|					|	+--	GraphicsView
#					|					|	|		>GraphicsItem
#					|					|	|		proxy = Typed(ProxyGraphicsView)
#					|					|	|		hug_width = set_default('ignore')
#					|					|	|		hug_height = set_default('ignore')
#					|					|	|		renderer = Enum('default', 'opengl', 'qwidget')
#					|					|	|		antialiasing = Bool(True)
#					|					|	|		selected_items = List(GraphicsItem)
#					|					|	|		drag_mode = Enum('none', 'scroll', 'selection')
#					|					|	|		min_zoom = Float(0.007, strict=False)
#					|					|	|		max_zoom = Float(100.0, strict=False)
#					|					|	|		auto_range = Bool(False)
#					|					|	|		lock_aspect_ratio = Bool(True)
#					|					|	|		extra_features = Coerced(GraphicFeature.Flags)
#					|					|	|		#
#					|					|	|		self.get_item_at(*args, **kwargs)
#					|					|	|		self.fit_in_view(item)
#					|					|	|		self.center_on(item)
#					|					|	|		self.translate_view(x=0, y=0)
#					|					|	|		self.scale_view(x=1, y=1)
#					|					|	|		self.rotate_view(angle=0)
#					|					|	|		self.reset_view()
#					|					|	|		self.map_from_scene(point)
#					|					|	|		self.map_to_scene(point)
#					|					|	|		self.pixel_density(self)
#					|					|	|		#
#					|					|	|		wheel_event => (event):
#					|					|	|		mouse_press_event => (event):
#					|					|	|		mouse_move_event => (event):
#					|					|	|		mouse_release_event => (event):
#					|					|	|		draw_background => (painter, rect):
#	widgets			|					|	+--	KeyEvent
#					|					|	|		proxy = Typed(ProxyKeyEvent))
#					|					|	|		keys = List(str)
#					|					|	|		enabled = Bool(True)
#					|					|	|		repeats = Bool(True)
#	widgets			|					|	+--	OccViewer
#					|					|	|		proxy = Typed(ProxyOccViewer)
#					|					|	|		position = Tuple(Int(strict=False),default=(0,0))
#					|					|	|		display_mode = Enum('shaded','hlr','wireframe')
#					|					|	|		selection_mode = Enum('shape','neutral','face','edge','vertex')
#					|					|	|		selection = List()
#					|					|	|		view_mode = Enum('iso','top','bottom','left','right','front','rear')
#					|					|	|		trihedron_mode = Enum('right-lower','disabled')
#					|					|	|		background_gradient = Tuple(Int(),default=(206, 215, 222, 128, 128, 128))
#					|					|	|		double_buffer = Bool(True)
#					|					|	|		shadows = Bool(False)
#					|					|	|		reflections = Bool(True)
#					|					|	|		antialiasing = Bool(True)
#					|					|	|		hug_width = set_default('ignore')
#					|					|	|		hug_height = set_default('ignore')
#					|					|	|		#
#					|					|	|		on_key_press :: Event()
#					|					|	|		on_mouse_press :: Event()
#					|					|	|		on_mouse_release :: Event()
#					|					|	|		on_mouse_wheel :: Event()
#					|					|	|		on_mouse_move :: Event()
#					|					|	+--	PlotItem
#					|					|	|	|	title = Str()
#					|					|	|	|	name = Str()
#					|					|	|	|	row = Int(0)
#					|					|	|	|	column = Int(0)
#					|					|	|	|	line_pen = Instance(PEN_ARGTYPES)
#					|					|	|	|	shadow_pen = Instance(PEN_ARGTYPES)
#					|					|	|	|	fill_level = Float(strict=False)
#					|					|	|	|	fill_brush = Instance(BRUSH_ARGTYPES)
#					|					|	|	|	symbol = Enum(None, 'o', 's', 't', 'd', '+')
#					|					|	|	|	symbol_size = Float(10, strict=False)
#					|					|	|	|	symbol_pen = Instance(PEN_ARGTYPES)
#					|					|	|	|	symbol_brush = Instance(BRUSH_ARGTYPES)
#					|					|	|	|	show_legend = ContainerList()
#					|					|	|	|	label_left = Str()
#					|					|	|	|	label_right = Str()
#					|					|	|	|	label_top = Str()
#					|					|	|	|	label_bottom = Str()
#					|					|	|	|	grid = Tuple(bool, default=(False, False))
#					|					|	|	|	grid_alpha = FloatRange(low=0.0, high=1.0, value=0.5)
#					|					|	|	|	multi_axis = Bool(True)
#					|					|	|	|	axis_left_ticks = Callable()
#					|					|	|	|	axis_bottom_ticks = Callable()
#					|					|	|	|	log_mode = Tuple(bool, default=(False, False))
#					|					|	|	|	antialias = Bool(False)
#					|					|	|	|	auto_range = Enum(True, False)
#					|					|	|	|	range_x = ContainerList(default=[0, 100])
#					|					|	|	|	range_y = ContainerList(default=[0, 100])
#					|					|	|	|	auto_downsample = Bool(False)
#					|					|	|	|	clip_to_view = Bool(False)
#					|					|	|	|	step_mode = Bool(False)
#					|					|	|	|	aspect_locked = Bool(False)
#					|					|	|	|	refresh_time = Int(100)
#	widgets			|					|	|	+--	PlotItem2D
#					|					|	|	|	|	x = ContainerList()
#					|					|	|	|	|	y = ContainerList()
#	widgets			|					|	|	|	+--	PlotItem3D
#					|					|	|	|	|	|	z = ContainerList()
#	widgets			|					|	|	|	|	+--	PlotItemArray3D
#					|					|	|	|	|			type = Enum('line')
#					|					|	|	|	|			x = numpy_ndarray
#					|					|	|	|	|			y = numpy_ndarray
#					|					|	|	|	|			z = numpy_ndarray
#	widgets			|					|	|	|	+--	PlotItemArray
#					|					|	|	|			x = numpy_ndarray
#					|					|	|	|			y = numpy_ndarray
#					|					|	|	+--	AbstractDataPlotItem
#	widgets			|					|	|		+--	PlotItemDict
#					|					|	|		|		data = Dict(default={'x': [], 'y': []})
#	widgets			|					|	|		+--	PlotItemList
#					|					|	|				data = ContainerList()
#	(enaml)			|					|	+--	SpinBox
#	widgets			|					|		+--	DoubleSpinBox
#					|					|				decimals = Int(2)
#					|					|				minimum = Float(0, strict=False)
#					|					|				maximum = Float(100, strict=False)
#					|					|				single_step = Float(1.0, strict=False)
#					|					|				value = Float(0, strict=False)
#	(enaml)			|					+--	Frame
#	(enaml)			|						+--	Container
#	widgets			|							+--	Console
#					|							|		proxy = Typed(ProxyConsole)
#					|							|		font_family = Str()
#					|							|		font_size = Int(0)
#					|							|		console_size = Coerced(Size,(81,25))
#					|							|		buffer_size = Int(0)
#					|							|		display_banner = Bool(False)
#					|							|		completion = Enum('ncurses','plain', 'droplist')
#					|							|		execute = Instance(object)
#	widgets			|							+--	PlotArea
#					|									hug_width = set_default('ignore')
#					|									hug_height = set_default('ignore')
#					|									proxy = Typed(ProxyPlotArea)
#					|									setup = Callable(lambda graph: None)
#	widgets			+--	Pen
#					|		color = ColorMember()
#					|		width = Float(1.0, strict=False)
#					|		line_style = Enum('solid', 'dash', 'dot', 'dash_dot', 'dash_dot_dot', 'custom', 'none')
#					|		cap_style = Enum('square', 'flat', 'round')
#					|		join_style = Enum('bevel', 'miter', 'round')
#					|		dash_pattern = List(Float(strict=False))
#	widgets			+--	Point
#					|		x = Float(0, strict=False)
#					|		y = Float(0, strict=False)
#					|		z = Float(0, strict=False)
#	widgets			+--	Rect
#							x = Float(0, strict=False)
#							y = Float(0, strict=False)
#							width = Float(0, strict=False)
#							height = Float(0, strict=False)

# Dependencies and relationship

#	(enaml)
#	+--	(Container)
#		+--	GraphicsView
#		|	|	>Point
#		|	|	>Rect
#		|	|	background =
#		|	|	drag_mode =
#		|	|	minimum_size =
#		|	+--	(AbstractGraphicsShapeItem)
#		|	|		>Brush
#		|	|		>Pen
#		|	+--	(Menu)
#		|	+--	(Pattern)
#		|	|	|	iterable = range(...)
#		|	|	|	loop.index
#		|	|	+--	GraphicsEllipseItem
#		|	|	|		height =
#		|	|	|		opacity =
#		|	|	|		pen =
#		|	|	|		position =
#		|	|	|		width =
#		|	|	+--	GraphicsLineItem
#		|	|	|		point =
#		|	|	|		position =
#		|	|	+--	GraphicsPathItem
#		|	|	|		pen =
#		|	|	|		movable =
#		|	|	|		path <<
#		|	|	|		scale =
#		|	|	+--	GraphicsPolygonItem
#		|	|	|		points =
#		|	|	|		scale =
#		|	|	+--	GraphicsRectItem
#		|	|	|		brush =
#		|	|	|		position =
#		|	|	|		opacity =
#		|	|	|		width =
#		|	|	+--	GraphicsTextItem
#		|	|			activated ::
#		|	|			drag_start => ():
#		|	|			drag_end => (drag_data, result):
#		|	|			features =
#		|	|			pen =
#		|	|			position =
#		|	|			rotation =
#		|	|			selectable =
#		|	|			text <<
#		|	+--	GraphicsImageItem
#		|	+--	GraphicsItemGroup
#		|	|	+--	(Pattern)
#		|	|		|	iterable = range(...)
#		|	|		|	loop.index
#		|	|		+--	(Graphics...Item)
#		|	+--	GraphicsWidget
#		|		|	position =
#		|		|	rotation =
#		|		+--	(Widget)
#		+--	PlotArea
#		|	+--	PlotItemArray
#		|		|	auto_range =
#		|		|	background =
#		|		|	label_left =
#		|		|	label_right =
#		|		|	line_pen =
#		|		|	multi_axis =
#		|		|	y <<
#		|		+--	(PlotItem...)
#		|			+--	(PlotItem...)
#		+--	TableView: table:
#		|	|	horizontal_headers <<
#		|	|	horizontal_stretch = True
#		|	|	items <<
#		|	|	minimum_size =
#		|	+--	(Pattern)
#		|		|	iterable <<
#		|		|	loop.index
#		|		|	loop.item
#		|		+--	TableViewRow
#		|			|	row << table.items[self.row]
#		|			|	clicked :=
#		|			+--	(Menu)
#		|			+--	TableViewItem
#		|				|	checkable =
#		|				|	checked :=
#		|				|	clicked :=
#		|				|	double_clicked :=
#		|				|	selected :=
#		|				|	icon <<
#		|				|	text <<
#		|				+--	(Control)
#		|				+--	(Menu)
#		|					+--	(Action)
#		|						text <<
#		|						triggered ::
#		+--	TreeView: tree:
#			|	horizontal_headers <<
#			|	items <<
#			+--	(Pattern)
#				|	iterable << tree.items
#				|	loop.index
#				|	loop.item
#				+--	TreeViewItem
#					|	icon <<
#					|	items <<
#					|	text <<
#					+--	(TreeViewItem)
#					+--	(TreeViewColumn)
#						|	checkable =
#						|	checked :=
#						|	icon <<
#						|	text <<
#						+--	(Control)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : AbstractItemView

from enamlx.widgets.abstract_item_view import AbstractItemView

	AbstractItemView:
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		items = ContainerList(default=[])
		selection_mode = Enum('extended', 'none', 'multi', 'single', 'contiguous')
		selection_behavior = Enum('items', 'rows', 'columns')
		selection = ContainerList(default=[])
		scroll_to_bottom = Bool(False)
		alternating_row_colors = Bool(False)
		cell_padding = Int(0)
		auto_resize = Bool(True)
		resize_mode = Enum('interactive', 'fixed', 'stretch', 'resize_to_contents', 'custom')
		word_wrap = Bool(False)
		show_vertical_header = Bool(True)
		vertical_headers = ContainerList()
		vertical_stretch = Bool(False)
		vertical_minimum_section_size = Int(0)
		show_horizontal_header = Bool(True)
		horizontal_headers << ContainerList()
		horizontal_stretch = Bool(False)
		horizontal_minimum_section_size = Int(0)
		sortable = Bool(True)
		current_row = Int(0)
		current_column = Int(0)
		visible_row = Int(0)
		visible_rows = Int(100)
		visible_column = Int(0)
		visible_columns = Int(1)
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
		self.layout_constraints()
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

#
# << (Control) :
aiview = AbstractItemView()

# <-> (set_default('ignore')) : Table should expand by default
hug_width = aiview.hug_width = hug_width

# <-> (set_default('ignore')) : Table should expand by default
hug_height = aiview.hug_height = hug_height

# <-> (ContainerList(default=[])) : The items to display in the view
items = aiview.items = items

# <-> (Enum('extended', 'none', 'multi', 'single', 'contiguous')) : Selection mode of the view
selection_mode = aiview.selection_mode = selection_mode

# <-> (Enum('items', 'rows', 'columns')) : Selection behavior of the view
selection_behavior = aiview.selection_behavior = selection_behavior

# <-> (ContainerList(default=[])) : Selection
selection = aiview.selection = selection

# <-> (Bool(False)) : Automatically scroll to bottm when new items are added
scroll_to_bottom = aiview.scroll_to_bottom = scroll_to_bottom

# <-> (Bool(False)) : Set alternating row colors
alternating_row_colors = aiview.alternating_row_colors = alternating_row_colors

# <-> (Int(0)) : Cell padding
cell_padding = aiview.cell_padding = cell_padding

# <-> (Bool(True)) : Automatically resize columns to fit contents
auto_resize = aiview.auto_resize = auto_resize

# <-> (Enum('interactive', 'fixed', 'stretch', 'resize_to_contents', 'custom')) : Resize mode of columns and rows
resize_mode = aiview.resize_mode = resize_mode

# <-> (Bool(False)) : Word wrap
word_wrap = aiview.word_wrap = word_wrap

# <-> (Bool(True)) : Show vertical header bar
show_vertical_header = aiview.show_vertical_header = show_vertical_header

# <-> (ContainerList()) : Row headers
vertical_headers = aiview.vertical_headers = vertical_headers

# <-> (Bool(False)) : Stretch last row
vertical_stretch = aiview.vertical_stretch = vertical_stretch

# <-> (Int(0)) : Minimum row size
vertical_minimum_section_size = aiview.vertical_minimum_section_size = vertical_minimum_section_size

# <-> (Bool(True)) : Show horizontal hearder bar
show_horizontal_header = aiview.show_horizontal_header = show_horizontal_header

# <-> (ContainerList()) : Column headers
horizontal_headers = aiview.horizontal_headers = horizontal_headers

# <-> (Bool(False)) : Stretch last column
horizontal_stretch = aiview.horizontal_stretch = horizontal_stretch

# <-> (Int(0)) : Minimum column size
horizontal_minimum_section_size = aiview.horizontal_minimum_section_size = horizontal_minimum_section_size

# <-> (Bool(True)) : Table is sortable
sortable = aiview.sortable = sortable

# <-> (Int(0)) : Current row index
current_row = aiview.current_row = current_row

# <-> (Int(0)) : Current column index
current_column = aiview.current_column = current_column

# <-> (Int(0)) : First visible row
visible_row = aiview.visible_row = visible_row

# <-> (Int(100)) : Number of rows visible
visible_rows = aiview.visible_rows = visible_rows

# <-> (Int(0)) : First visible column
visible_column = aiview.visible_column = visible_column

# <-> (Int(1)) : Number of columns visible
visible_columns = aiview.visible_columns = visible_columns

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

from enamlx.widgets.abstract_item import AbstractWidgetItemGroup

	AbstractWidgetItemGroup:
		clicked :: Event()
		double_clicked :: Event()
		entered :: Event()
		pressed :: Event()
		selection_changed :: Event(bool)
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
		self.layout_constraints()
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

#
# << (Control) :
awigroup = AbstractWidgetItemGroup()

# <-> (Event()) : Triggered when clicked
clicked = awigroup.clicked = clicked

# <-> (Event()) : Triggered when double clicked
double_clicked = awigroup.double_clicked = double_clicked

# <-> (Event()) : Triggered when the row, column, or item is entered
entered = awigroup.entered = entered

# <-> (Event()) : Triggered when the row, column, or item is pressed
pressed = awigroup.pressed = pressed

# <-> (Event(bool)) : Triggered when the row, column, or item's selection changes
selection_changed = awigroup.selection_changed = selection_changed

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

from enamlx.widgets.abstract_item import AbstractWidgetItem

	AbstractWidgetItem:
		row = Int()
		column = Int()
		text = Str()
		text_alignment = Enum(*[(h, v) for h in ('left', 'right', 'center', 'justify') for v in ('center', 'top', 'bottom')])
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		selectable = Bool(True)
		selected = Bool()
		checkable = Bool()
		checked = Bool()
		editable = Bool()
		changed :: Event()
		toggled :: Event(bool)
			#AbstractWidgetItemGroup:
		clicked :: Event()
		double_clicked :: Event()
		entered :: Event()
		pressed :: Event()
		selection_changed :: Event(bool)
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
		self.layout_constraints()
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

#
# << (AbstractWidgetItemGroup) :
awitem = AbstractWidgetItem()

# <-> (Int()) : Model index or row within the view
row = awitem.row = row

# <-> (Int()) : Column within the view
column = awitem.column = column

# <-> (Str()) : Text to display within the cell
text = awitem.text = text

# <-> (Enum(*[(h, v) for h in ('left', 'right', 'center', 'justify') for v in ('center', 'top', 'bottom')])) : Text alignment within the cell
text_alignment = awitem.text_alignment = text_alignment

# <-> (Typed(Icon)) : Icon to display in the cell
icon = awitem.icon = icon

# <-> (Coerced(Size, (-1, -1))) : The size to use for the icon
icon_size = awitem.icon_size = icon_size

# <-> (Bool(True)) : Whether the item or group can be selected
selectable = awitem.selectable = selectable

# <-> (Bool()) : Selection state of the item or group
selected = awitem.selected = selected

# <-> (Bool()) : Whether the item or group can be checked
checkable = awitem.checkable = checkable

# <-> (Bool()) : Checked state of the item or group
checked = awitem.checked = checked

# <-> (Bool()) : Whether the item or group can be edited
editable = awitem.editable = editable

# <-> (Event()) : Triggered when the item's contents change
changed = awitem.changed = changed

# <-> (Event(bool)) : Triggered when the checkbox state changes
toggled = awitem.toggled = toggled

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : TableView

from enamlx.widgets.api import TableView

	TableView:
		proxy = Typed(ProxyTableView)
		show_grid = Bool(True)
			#AbstractItemView:
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		items = ContainerList(default=[])
		selection_mode = Enum('extended', 'none', 'multi', 'single', 'contiguous')
		selection_behavior = Enum('items', 'rows', 'columns')
		selection = ContainerList(default=[])
		scroll_to_bottom = Bool(False)
		alternating_row_colors = Bool(False)
		cell_padding = Int(0)
		auto_resize = Bool(True)
		resize_mode = Enum('interactive', 'fixed', 'stretch', 'resize_to_contents', 'custom')
		word_wrap = Bool(False)
		show_vertical_header = Bool(True)
		vertical_headers = ContainerList()
		vertical_stretch = Bool(False)
		vertical_minimum_section_size = Int(0)
		show_horizontal_header = Bool(True)
		horizontal_headers << ContainerList()
		horizontal_stretch = Bool(False)
		horizontal_minimum_section_size = Int(0)
		sortable = Bool(True)
		current_row = Int(0)
		current_column = Int(0)
		visible_row = Int(0)
		visible_rows = Int(100)
		visible_column = Int(0)
		visible_columns = Int(1)
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
		self.layout_constraints()
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

#
# << (AbstractItemView) :
tview = TableView()

# <-> (Typed(ProxyTableView)) : Proxy reference
proxy = tview.proxy = proxy

# <-> (Bool(True)) : Show grid of cells
show_grid = tview.show_grid = show_grid

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : TableViewItem

from enamlx.widgets.api import TableViewItem

	TableViewItem:
		proxy = Typed(ProxyTableViewItem)
			#AbstractWidgetItem:
		row = Int()
		column = Int()
		text = Str()
		text_alignment = Enum(*[(h, v) for h in ('left', 'right', 'center', 'justify') for v in ('center', 'top', 'bottom')])
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		selectable = Bool(True)
		selected = Bool()
		checkable = Bool()
		checked = Bool()
		editable = Bool()
		changed :: Event()
		toggled :: Event(bool)
			#AbstractWidgetItemGroup:
		clicked :: Event()
		double_clicked :: Event()
		entered :: Event()
		pressed :: Event()
		selection_changed :: Event(bool)
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
		self.layout_constraints()
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

#
# << (AbstractWidgetItem) :
tvitem = TableViewItem()

# <-> (Typed(ProxyTableViewItem)) : Proxy reference
proxy = tvitem.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : TableViewRow

from enamlx.widgets.api import TableViewRow

	TableViewRow:
		proxy = Typed(ProxyTableViewRow)
		row = Int()
			#AbstractWidgetItemGroup:
		clicked :: Event()
		double_clicked :: Event()
		entered :: Event()
		pressed :: Event()
		selection_changed :: Event(bool)
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
		self.layout_constraints()
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

#
# << (AbstractWidgetItemGroup) :
tvrow = TableViewRow()

# <-> (Typed(ProxyTableViewRow)) : Proxy reference
proxy = tvrow.proxy = proxy

# <-> (Int()) : Row within the table
row = tvrow.row = row

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : TableViewColumn

from enamlx.widgets.api import TableViewColumn

	TableViewColumn:
		proxy = Typed(ProxyTableViewColumn)
		column = Int()
			#AbstractWidgetItemGroup:
		clicked :: Event()
		double_clicked :: Event()
		entered :: Event()
		pressed :: Event()
		selection_changed :: Event(bool)
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
		self.layout_constraints()
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

#
# << (AbstractWidgetItemGroup) :
tvcol = TableViewColumn()

# <-> (Typed(ProxyTableViewColumn)) : Proxy reference
proxy = tvcol.proxy = proxy

# <-> (Int()) : Column within the table
column = tvcol.column = column

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : TreeView

from enamlx.widgets.api import TreeView

	TreeView:
		proxy = Typed(ProxyTreeView)
		show_root = Bool(True)
			#AbstractItemView:
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		items = ContainerList(default=[])
		selection_mode = Enum('extended', 'none', 'multi', 'single', 'contiguous')
		selection_behavior = Enum('items', 'rows', 'columns')
		selection = ContainerList(default=[])
		scroll_to_bottom = Bool(False)
		alternating_row_colors = Bool(False)
		cell_padding = Int(0)
		auto_resize = Bool(True)
		resize_mode = Enum('interactive', 'fixed', 'stretch', 'resize_to_contents', 'custom')
		word_wrap = Bool(False)
		show_vertical_header = Bool(True)
		vertical_headers = ContainerList()
		vertical_stretch = Bool(False)
		vertical_minimum_section_size = Int(0)
		show_horizontal_header = Bool(True)
		horizontal_headers << ContainerList()
		horizontal_stretch = Bool(False)
		horizontal_minimum_section_size = Int(0)
		sortable = Bool(True)
		current_row = Int(0)
		current_column = Int(0)
		visible_row = Int(0)
		visible_rows = Int(100)
		visible_column = Int(0)
		visible_columns = Int(1)
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
		self.layout_constraints()
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

#
# << (AbstractItemView) :
tview = TreeView()

# <-> (Typed(ProxyTreeView)) : Proxy reference
proxy = tview.proxy = proxy

# <-> (Bool(True)) : Show root node
show_root = tview.show_root = show_root

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : TreeViewItem

from enamlx.widgets.api import TreeViewItem

	TreeViewItem:
		proxy = Typed(ProxyTreeViewItem)
		items = ContainerList(default=[])
		visible_row = Int(0)
		visible_rows = Int(100)
		visible_column = Int(0)
		visible_columns = Int(1)
			#AbstractWidgetItem:
		row = Int()
		column = Int()
		text = Str()
		text_alignment = Enum(*[(h, v) for h in ('left', 'right', 'center', 'justify') for v in ('center', 'top', 'bottom')])
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		selectable = Bool(True)
		selected = Bool()
		checkable = Bool()
		checked = Bool()
		editable = Bool()
		changed :: Event()
		toggled :: Event(bool)
			#AbstractWidgetItemGroup:
		clicked :: Event()
		double_clicked :: Event()
		entered :: Event()
		pressed :: Event()
		selection_changed :: Event(bool)
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
		self.layout_constraints()
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

#
# << (AbstractWidgetItem) :
tvitem = TreeViewItem()

# <-> (Typed(ProxyTreeViewItem)) : Proxy reference
proxy = tvitem.proxy = proxy

# <-> (ContainerList(default=[])) : The child items
items = tvitem.items = items

# <-> (Int(0)) : First visible row
visible_row = tvitem.visible_row = visible_row

# <-> (Int(100)) : Number of rows visible
visible_rows = tvitem.visible_rows = visible_rows

# <-> (Int(0)) : First visible column
visible_column = tvitem.visible_column = visible_column

# <-> (Int(1)) : Number of columns visible
visible_columns = tvitem.visible_columns = visible_columns

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : TreeViewColumn

from enamlx.widgets.api import TreeViewColumn

	TreeViewColumn:
		proxy = Typed(ProxyTreeViewColumn)
			#AbstractWidgetItem:
		row = Int()
		column = Int()
		text = Str()
		text_alignment = Enum(*[(h, v) for h in ('left', 'right', 'center', 'justify') for v in ('center', 'top', 'bottom')])
		icon = Typed(Icon)
		icon_size = Coerced(Size, (-1, -1))
		selectable = Bool(True)
		selected = Bool()
		checkable = Bool()
		checked = Bool()
		editable = Bool()
		changed :: Event()
		toggled :: Event(bool)
			#AbstractWidgetItemGroup:
		clicked :: Event()
		double_clicked :: Event()
		entered :: Event()
		pressed :: Event()
		selection_changed :: Event(bool)
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
		self.layout_constraints()
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

#
# << (AbstractWidgetItem) :
tvcol = TreeViewColumn()

# <-> (Typed(ProxyTreeViewColumn)) : Proxy reference
proxy = tvcol.proxy = proxy

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : PlotArea

from enamlx.widgets.api import PlotArea

	PlotArea:
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		proxy = Typed(ProxyPlotArea)
		setup = Callable(lambda graph: None)
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
		self.layout_constraints()
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

#
# << (Container) :
parea = PlotArea()

# <-> (set_default('ignore')) :
hug_width = parea.hug_width = hug_width

# <-> (set_default('ignore')) :
hug_height = parea.hug_height = hug_height

# <-> (Typed(ProxyPlotArea)) :
proxy = parea.proxy = proxy

# <-> (Callable(lambda graph: None)) :
setup = parea.setup = setup

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : PlotItem

from enamlx.widgets.plot_area import PlotItem

	PlotItem:
		title = Str()
		name = Str()
		row = Int(0)
		column = Int(0)
		line_pen = Instance(PEN_ARGTYPES)
		shadow_pen = Instance(PEN_ARGTYPES)
		fill_level = Float(strict=False)
		fill_brush = Instance(BRUSH_ARGTYPES)
		symbol = Enum(None, 'o', 's', 't', 'd', '+')
		symbol_size = Float(10, strict=False)
		symbol_pen = Instance(PEN_ARGTYPES)
		symbol_brush = Instance(BRUSH_ARGTYPES)
		show_legend = ContainerList()
		label_left = Str()
		label_right = Str()
		label_top = Str()
		label_bottom = Str()
		grid = Tuple(bool, default=(False, False))
		grid_alpha = FloatRange(low=0.0, high=1.0, value=0.5)
		multi_axis = Bool(True)
		axis_left_ticks = Callable()
		axis_bottom_ticks = Callable()
		log_mode = Tuple(bool, default=(False, False))
		antialias = Bool(False)
		auto_range = Enum(True, False)
		range_x = ContainerList(default=[0, 100])
		range_y = ContainerList(default=[0, 100])
		auto_downsample = Bool(False)
		clip_to_view = Bool(False)
		step_mode = Bool(False)
		aspect_locked = Bool(False)
		refresh_time = Int(100)
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
		self.layout_constraints()
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

#
# << (Control) :
pitem = PlotItem()

# <-> (Str()) : Title of data series
title = pitem.title = title

# <-> (Str()) : Name
name = pitem.name = name

# <-> (Int(0)) : Row in plot area
row = pitem.row = row

# <-> (Int(0)) : Column in plot area
column = pitem.column = column

# <-> (Instance(PEN_ARGTYPES)) : Pen type to use for line
line_pen = pitem.line_pen = line_pen

# <-> (Instance(PEN_ARGTYPES)) : Pen type to use for shadow
shadow_pen = pitem.shadow_pen = shadow_pen

# <-> (Float(strict=False)) : Fill level
fill_level = pitem.fill_level = fill_level

# <-> (Instance(BRUSH_ARGTYPES)) : Brush fill type
fill_brush = pitem.fill_brush = fill_brush

# <-> (Enum(None, 'o', 's', 't', 'd', '+')) : Symbol to use for points
symbol = pitem.symbol = symbol

# <-> (Float(10, strict=False)) : Symbol sizes for points
symbol_size = pitem.symbol_size = symbol_size

# <-> (Instance(PEN_ARGTYPES)) : Symbol pen to use
symbol_pen = pitem.symbol_pen = symbol_pen

# <-> (Instance(BRUSH_ARGTYPES)) : Symbol brush
symbol_brush = pitem.symbol_brush = symbol_brush

# <-> (ContainerList()) : Show legend
show_legend = pitem.show_legend = show_legend

# <-> (Str()) :
label_left = pitem.label_left = label_left

# <-> (Str()) :
label_right = pitem.label_right = label_right

# <-> (Str()) :
label_top = pitem.label_top = label_top

# <-> (Str()) :
label_bottom = pitem.label_bottom = label_bottom

# <-> (Tuple(bool, default=(False, False))) : H, V
grid = pitem.grid = grid

# <-> (FloatRange(low=0.0, high=1.0, value=0.5)) : H, V
grid_alpha = pitem.grid_alpha = grid_alpha

# <-> (Bool(True)) : Display a separate axis for each nested plot
multi_axis = pitem.multi_axis = multi_axis

# <-> (Callable()) :
axis_left_ticks = pitem.axis_left_ticks = axis_left_ticks

# <-> (Callable()) :
axis_bottom_ticks = pitem.axis_bottom_ticks = axis_bottom_ticks

# <-> (Tuple(bool, default=(False, False))) : Display the axis on log scale
log_mode = pitem.log_mode = log_mode

# <-> (Bool(False)) : Enable antialiasing
antialias = pitem.antialias = antialias

# <-> (Enum(True, False)) : Set auto range for each axis
auto_range = pitem.auto_range = auto_range

# <-> (ContainerList(default=[0, 100])) : x-range to use if auto_range is disabled
range_x = pitem.range_x = range_x

# <-> (ContainerList(default=[0, 100])) : y-range to use if auto_range is disabled
range_y = pitem.range_y = range_y

# <-> (Bool(False)) : Automatically downsaple
auto_downsample = pitem.auto_downsample = auto_downsample

# <-> (Bool(False)) : Clip data points to view
clip_to_view = pitem.clip_to_view = clip_to_view

# <-> (Bool(False)) : Step mode to use
step_mode = pitem.step_mode = step_mode

# <-> (Bool(False)) : Keep aspect ratio locked when resizing
aspect_locked = pitem.aspect_locked = aspect_locked

# <-> (Int(100)) : Time between updates
refresh_time = pitem.refresh_time = refresh_time

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : PlotItem2D

from enamlx.widgets.api import PlotItem2D

	PlotItem2D:
		x = ContainerList()
		y = ContainerList()
			#PlotItem:
		title = Str()
		name = Str()
		row = Int(0)
		column = Int(0)
		line_pen = Instance(PEN_ARGTYPES)
		shadow_pen = Instance(PEN_ARGTYPES)
		fill_level = Float(strict=False)
		fill_brush = Instance(BRUSH_ARGTYPES)
		symbol = Enum(None, 'o', 's', 't', 'd', '+')
		symbol_size = Float(10, strict=False)
		symbol_pen = Instance(PEN_ARGTYPES)
		symbol_brush = Instance(BRUSH_ARGTYPES)
		show_legend = ContainerList()
		label_left = Str()
		label_right = Str()
		label_top = Str()
		label_bottom = Str()
		grid = Tuple(bool, default=(False, False))
		grid_alpha = FloatRange(low=0.0, high=1.0, value=0.5)
		multi_axis = Bool(True)
		axis_left_ticks = Callable()
		axis_bottom_ticks = Callable()
		log_mode = Tuple(bool, default=(False, False))
		antialias = Bool(False)
		auto_range = Enum(True, False)
		range_x = ContainerList(default=[0, 100])
		range_y = ContainerList(default=[0, 100])
		auto_downsample = Bool(False)
		clip_to_view = Bool(False)
		step_mode = Bool(False)
		aspect_locked = Bool(False)
		refresh_time = Int(100)
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
		self.layout_constraints()
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

#
# << (PlotItem) :
pi2d = PlotItem2D()

# <-> (ContainerList()) : x-axis values, as a list
x = pi3d.x = x

# <-> (ContainerList()) : y-axis values, as a list
y = pi3d.y = y

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : PlotItem3D

from enamlx.widgets.api import PlotItem3D

	PlotItem3D:
		z = ContainerList()
			#PlotItem2D:
		x = ContainerList()
		y = ContainerList()
			#PlotItem:
		title = Str()
		name = Str()
		row = Int(0)
		column = Int(0)
		line_pen = Instance(PEN_ARGTYPES)
		shadow_pen = Instance(PEN_ARGTYPES)
		fill_level = Float(strict=False)
		fill_brush = Instance(BRUSH_ARGTYPES)
		symbol = Enum(None, 'o', 's', 't', 'd', '+')
		symbol_size = Float(10, strict=False)
		symbol_pen = Instance(PEN_ARGTYPES)
		symbol_brush = Instance(BRUSH_ARGTYPES)
		show_legend = ContainerList()
		label_left = Str()
		label_right = Str()
		label_top = Str()
		label_bottom = Str()
		grid = Tuple(bool, default=(False, False))
		grid_alpha = FloatRange(low=0.0, high=1.0, value=0.5)
		multi_axis = Bool(True)
		axis_left_ticks = Callable()
		axis_bottom_ticks = Callable()
		log_mode = Tuple(bool, default=(False, False))
		antialias = Bool(False)
		auto_range = Enum(True, False)
		range_x = ContainerList(default=[0, 100])
		range_y = ContainerList(default=[0, 100])
		auto_downsample = Bool(False)
		clip_to_view = Bool(False)
		step_mode = Bool(False)
		aspect_locked = Bool(False)
		refresh_time = Int(100)
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
		self.layout_constraints()
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

#
# << (PlotItem2D) :
pi3d = PlotItem3D()

# <-> (ContainerList()) : z-axis values, as a list
z = pi3d.z = z

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : PlotItemArray

from enamlx.widgets.api import PlotItemArray

	PlotItemArray:
		x << numpy_ndarray
		y << numpy_ndarray
			#PlotItem2D:
		x = ContainerList()
		y = ContainerList()
			#PlotItem:
		title = Str()
		name = Str()
		row = Int(0)
		column = Int(0)
		line_pen = Instance(PEN_ARGTYPES)
		shadow_pen = Instance(PEN_ARGTYPES)
		fill_level = Float(strict=False)
		fill_brush = Instance(BRUSH_ARGTYPES)
		symbol = Enum(None, 'o', 's', 't', 'd', '+')
		symbol_size = Float(10, strict=False)
		symbol_pen = Instance(PEN_ARGTYPES)
		symbol_brush = Instance(BRUSH_ARGTYPES)
		show_legend = ContainerList()
		label_left = Str()
		label_right = Str()
		label_top = Str()
		label_bottom = Str()
		grid = Tuple(bool, default=(False, False))
		grid_alpha = FloatRange(low=0.0, high=1.0, value=0.5)
		multi_axis = Bool(True)
		axis_left_ticks = Callable()
		axis_bottom_ticks = Callable()
		log_mode = Tuple(bool, default=(False, False))
		antialias = Bool(False)
		auto_range = Enum(True, False)
		range_x = ContainerList(default=[0, 100])
		range_y = ContainerList(default=[0, 100])
		auto_downsample = Bool(False)
		clip_to_view = Bool(False)
		step_mode = Bool(False)
		aspect_locked = Bool(False)
		refresh_time = Int(100)
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
		self.layout_constraints()
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

# Numpy array item
# << (PlotItem2D) :
piarr2d = PlotItemArray()

# <-> (numpy_ndarray) : x-axis values, as a numpy array
x = piarr2d.x = x

# <-> (numpy_ndarray) : y-axis values, as a numpy array
y = piarr2d.y = y

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : PlotItemArray3D

from enamlx.widgets.api import PlotItemArray3D

	PlotItemArray3D:
		type = Enum('line')
		x << numpy_ndarray
		y << numpy_ndarray
		z << numpy_ndarray
			#PlotItem3D:
		z = ContainerList()
			#PlotItem2D:
		x = ContainerList()
		y = ContainerList()
			#PlotItem:
		title = Str()
		name = Str()
		row = Int(0)
		column = Int(0)
		line_pen = Instance(PEN_ARGTYPES)
		shadow_pen = Instance(PEN_ARGTYPES)
		fill_level = Float(strict=False)
		fill_brush = Instance(BRUSH_ARGTYPES)
		symbol = Enum(None, 'o', 's', 't', 'd', '+')
		symbol_size = Float(10, strict=False)
		symbol_pen = Instance(PEN_ARGTYPES)
		symbol_brush = Instance(BRUSH_ARGTYPES)
		show_legend = ContainerList()
		label_left = Str()
		label_right = Str()
		label_top = Str()
		label_bottom = Str()
		grid = Tuple(bool, default=(False, False))
		grid_alpha = FloatRange(low=0.0, high=1.0, value=0.5)
		multi_axis = Bool(True)
		axis_left_ticks = Callable()
		axis_bottom_ticks = Callable()
		log_mode = Tuple(bool, default=(False, False))
		antialias = Bool(False)
		auto_range = Enum(True, False)
		range_x = ContainerList(default=[0, 100])
		range_y = ContainerList(default=[0, 100])
		auto_downsample = Bool(False)
		clip_to_view = Bool(False)
		step_mode = Bool(False)
		aspect_locked = Bool(False)
		refresh_time = Int(100)
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
		self.layout_constraints()
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

# Numpy array item
# << (PlotItem3D) :
piarr3d = PlotItemArray3D()

# <-> (Enum('line')) : Plot type
type = piarr3d.type = type

# <-> (numpy_ndarray) : x-axis values, as a numpy array
x = piarr3d.x = x

# <-> (numpy_ndarray) : y-axis values, as a numpy array
y = piarr3d.y = y

# <-> (numpy_ndarray) : z-axis values, as a numpy array
z = piarr3d.z = z

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : PlotItemDict

from enamlx.widgets.api import PlotItemDict

	PlotItemDict:
		data = Dict(default={'x': [], 'y': []})
			#AbstractDataPlotItem:
			#PlotItem:
		title = Str()
		name = Str()
		row = Int(0)
		column = Int(0)
		line_pen = Instance(PEN_ARGTYPES)
		shadow_pen = Instance(PEN_ARGTYPES)
		fill_level = Float(strict=False)
		fill_brush = Instance(BRUSH_ARGTYPES)
		symbol = Enum(None, 'o', 's', 't', 'd', '+')
		symbol_size = Float(10, strict=False)
		symbol_pen = Instance(PEN_ARGTYPES)
		symbol_brush = Instance(BRUSH_ARGTYPES)
		show_legend = ContainerList()
		label_left = Str()
		label_right = Str()
		label_top = Str()
		label_bottom = Str()
		grid = Tuple(bool, default=(False, False))
		grid_alpha = FloatRange(low=0.0, high=1.0, value=0.5)
		multi_axis = Bool(True)
		axis_left_ticks = Callable()
		axis_bottom_ticks = Callable()
		log_mode = Tuple(bool, default=(False, False))
		antialias = Bool(False)
		auto_range = Enum(True, False)
		range_x = ContainerList(default=[0, 100])
		range_y = ContainerList(default=[0, 100])
		auto_downsample = Bool(False)
		clip_to_view = Bool(False)
		step_mode = Bool(False)
		aspect_locked = Bool(False)
		refresh_time = Int(100)
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
		self.layout_constraints()
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

#
# << (AbstractDataPlotItem) :
pidict = PlotItemDict()

# <-> (Dict(default={'x': [], 'y': []})) :
data = pidict.data = data

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : PlotItemList

from enamlx.widgets.api import PlotItemList

	PlotItemList:
		data = ContainerList()
			#AbstractDataPlotItem:
			#PlotItem:
		title = Str()
		name = Str()
		row = Int(0)
		column = Int(0)
		line_pen = Instance(PEN_ARGTYPES)
		shadow_pen = Instance(PEN_ARGTYPES)
		fill_level = Float(strict=False)
		fill_brush = Instance(BRUSH_ARGTYPES)
		symbol = Enum(None, 'o', 's', 't', 'd', '+')
		symbol_size = Float(10, strict=False)
		symbol_pen = Instance(PEN_ARGTYPES)
		symbol_brush = Instance(BRUSH_ARGTYPES)
		show_legend = ContainerList()
		label_left = Str()
		label_right = Str()
		label_top = Str()
		label_bottom = Str()
		grid = Tuple(bool, default=(False, False))
		grid_alpha = FloatRange(low=0.0, high=1.0, value=0.5)
		multi_axis = Bool(True)
		axis_left_ticks = Callable()
		axis_bottom_ticks = Callable()
		log_mode = Tuple(bool, default=(False, False))
		antialias = Bool(False)
		auto_range = Enum(True, False)
		range_x = ContainerList(default=[0, 100])
		range_y = ContainerList(default=[0, 100])
		auto_downsample = Bool(False)
		clip_to_view = Bool(False)
		step_mode = Bool(False)
		aspect_locked = Bool(False)
		refresh_time = Int(100)
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
		self.layout_constraints()
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

#
# << (AbstractDataPlotItem) :
pilist = PlotItemList()

# <-> (ContainerList()) :
data = pilist.data = data

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : OccViewer

from enamlx.widgets.api import OccViewer

	OccViewer:
		proxy = Typed(ProxyOccViewer)
		position = Tuple(Int(strict=False),default=(0,0))
		display_mode = Enum('shaded','hlr','wireframe')
		selection_mode = Enum('shape','neutral','face','edge','vertex')
		selection = List()
		view_mode = Enum('iso','top','bottom','left','right','front','rear')
		trihedron_mode = Enum('right-lower','disabled')
		background_gradient = Tuple(Int(),default=(206, 215, 222, 128, 128, 128))
		double_buffer = Bool(True)
		shadows = Bool(False)
		reflections = Bool(True)
		antialiasing = Bool(True)
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		#
		on_key_press :: Event()
		on_mouse_press :: Event()
		on_mouse_release :: Event()
		on_mouse_wheel :: Event()
		on_mouse_move :: Event()
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
		self.layout_constraints()
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
occview = OccViewer()

# <-> (Typed(ProxyOccViewer)) : A reference to the ProxySpinBox object
proxy = occview.proxy = proxy

# <-> (Tuple(Int(strict=False),default=(0,0))) : The minimum value for the spin box
position = occview.position = position

# <-> (Enum('shaded','hlr','wireframe')) : Display mode
display_mode = occview.display_mode = display_mode

# <-> (Enum('shape','neutral','face','edge','vertex')) : Selection mode
selection_mode = occview.selection_mode = selection_mode

# -> (List()) : Selected items
selection = occview.selection

# <-> (Enum('iso','top','bottom','left','right','front','rear')) : View direction
view_mode = occview.view_mode = view_mode

# <-> (Enum('right-lower','disabled')) : Show tahedron
trihedron_mode = occview.trihedron_mode = trihedron_mode

# <-> (Tuple(Int(),default=(206, 215, 222, 128, 128, 128))) : Background gradient
background_gradient = occview.background_gradient = background_gradient

# <-> (Bool(True)) : Use double buffering
double_buffer = occview.double_buffer = double_buffer

# <-> (Bool(False)) : Display shadows
shadows = occview.shadows = shadows

# <-> (Bool(True)) : Display reflections
reflections = occview.reflections = reflections

# <-> (Bool(True)) : Enable antialiasing
antialiasing = occview.antialiasing = antialiasing

# <-> (set_default('ignore')) : View expands freely in width by default
hug_width = occview.hug_width = hug_width

# <-> (set_default('ignore')) : View expands freely in height by default
hug_height = occview.hug_height = hug_height

# -> (Event()) : Raise StopIteration to indicate handling should stop
on_key_press = occview.on_key_press

# -> (Event()) : Raise StopIteration to indicate handling should stop
on_mouse_press = occview.on_mouse_press

# -> (Event()) : Raise StopIteration to indicate handling should stop
on_mouse_release = occview.on_mouse_release

# -> (Event()) : Raise StopIteration to indicate handling should stop
on_mouse_wheel = occview.on_mouse_wheel

# -> (Event()) : Raise StopIteration to indicate handling should stop
on_mouse_move = occview.on_mouse_move

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : DoubleSpinBox

from enamlx.widgets.api import DoubleSpinBox

	DoubleSpinBox:
		decimals = Int(2)
		minimum = Float(0, strict=False)
		maximum = Float(100, strict=False)
		single_step = Float(1.0, strict=False)
		value = Float(0, strict=False)
			#SpinBox:
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
		self.layout_constraints()
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

# A spin box widget which manipulates float values
# << (SpinBox) :
dsbox = DoubleSpinBox()

# <-> (Int(2)) : The number of decmial places to be shown
decimals = dsbox.decimals = decimals

# <-> (Float(0, strict=False)) : The minimum value for the spin box
minimum = dsbox.minimum = minimum

# <-> (Float(100, strict=False)) : The maximum value for the spin box
maximum = dsbox.maximum = maximum

# <-> (Float(1.0, strict=False)) : The maximum value for the spin box
single_step = dsbox.single_step = single_step

# <-> (Float(0, strict=False)) : The position value of the spin box
value = dsbox.value = value

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : Console

from enamlx.widgets.api import Console

	Console:
		proxy = Typed(ProxyConsole)
		font_family = Str()
		font_size = Int(0)
		console_size = Coerced(Size,(81,25))
		buffer_size = Int(0)
		display_banner = Bool(False)
		completion = Enum('ncurses','plain', 'droplist')
		execute = Instance(object)
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
		self.layout_constraints()
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

# Console widget
# << (Container) :
cli = Console()

# <-> (Typed(ProxyConsole)) :
proxy = cli.proxy = proxy

# <-> (Str()) : Font family, leave blank for default
font_family = cli.font_family = font_family

# <-> (Int(0)) : Font size, leave 0 for default
font_size = cli.font_size = font_size

# <-> (Coerced(Size,(81,25))) : Default console size in characters
console_size = cli.console_size = console_size

# <-> (Int(0)) : Buffer size, leave 0 for default
buffer_size = cli.buffer_size = buffer_size

# <-> (Bool(False)) : Display banner like version, etc..
display_banner = cli.display_banner = display_banner

# <-> (Enum('ncurses','plain', 'droplist')) : Code completion type
completion = cli.completion = completion

# <-> (Instance(object)) : Run the line or callabla
execute = cli.execute = execute

# <- (Dict()) : Push variables to the console
scope = cli.scope

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : KeyEvent

from enamlx.widgets.api import KeyEvent

	KeyEvent:
		proxy = Typed(ProxyKeyEvent))
		keys = List(str)
		enabled = Bool(True)
		repeats = Bool(True)
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
		self.layout_constraints()
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

#
# << (Control) :
kevnt = KeyEvent()

# <-> (Typed(ProxyKeyEvent))) : Proxy reference
proxy = kevnt.proxy = proxy

# <-> (List(str)) : List of keys that or codes to filter
keys = kevnt.keys = keys

# <-> (Bool(True)) : Listen for events
enabled = kevnt.enabled = enabled

# <-> (Bool(True)) : Fire multiple times when the key is held
repeats = kevnt.repeats = repeats

# -> (Event(dict)) : Pressed event
pressed = kevnt.pressed

# -> (Event(dict)) : Released event
released = kevnt.released

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# EnamlX : GraphicsView

from enamlx.widgets.api import GraphicsView

	GraphicsView:
		proxy = Typed(ProxyGraphicsView)
		hug_width = set_default('ignore')
		hug_height = set_default('ignore')
		renderer = Enum('default', 'opengl', 'qwidget')
		antialiasing = Bool(True)
		selected_items = List(GraphicsItem)
		drag_mode = Enum('none', 'scroll', 'selection')
		min_zoom = Float(0.007, strict=False)
		max_zoom = Float(100.0, strict=False)
		auto_range = Bool(False)
		lock_aspect_ratio = Bool(True)
		extra_features = Coerced(GraphicFeature.Flags)
		#
		self.get_item_at(*args, **kwargs)
		self.fit_in_view(item)
		self.center_on(item)
		self.translate_view(x=0, y=0)
		self.scale_view(x=1, y=1)
		self.rotate_view(angle=0)
		self.reset_view()
		self.map_from_scene(point)
		self.map_to_scene(point)
		self.pixel_density(self)
		#
		wheel_event => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		draw_background => (painter, rect):
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
		self.layout_constraints()
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
#
# << (Control) :
gview = GraphicsView()

# <-> (Typed(ProxyGraphicsView)) : Proxy reference
proxy = gview.proxy = proxy

# <-> (set_default('ignore')) : An graphicsview widget expands freely in height and width by default
hug_width = gview.hug_width = hug_width

# <-> (set_default('ignore')) : An graphicsview widget expands freely in height and width by default
hug_height = gview.hug_height = hug_height

# <-> (Enum('default', 'opengl', 'qwidget')) : Select backend for rendering. OpenGL is used by default if available
renderer = gview.renderer = renderer

# <-> (Bool(True)) : Antialiasing is enabled by default
antialiasing = gview.antialiasing = antialiasing

# <-> (List(GraphicsItem)) : Items currently selected
selected_items = gview.selected_items = selected_items

# <-> (Enum('none', 'scroll', 'selection')) : Defines the behavior when dragging
drag_mode = gview.drag_mode = drag_mode

# <-> (Float(0.007, strict=False)) : Range of allowed zoom factors
min_zoom = gview.min_zoom = min_zoom

# <-> (Float(100.0, strict=False)) : Range of allowed zoom factors
max_zoom = gview.max_zoom = max_zoom

# <-> (Bool(False)) : Automatically resize view to fit the scene contents
auto_range = gview.auto_range = auto_range

# <-> (Bool(True)) : Keep the aspect ratio locked when resizing the view range
lock_aspect_ratio = gview.lock_aspect_ratio = lock_aspect_ratio

# <-> (Coerced(GraphicFeature.Flags)) : Set the extra features to enable for this widget
extra_features = gview.extra_features = extra_features

# A method invoked when a wheel event occurs in the widget (to be reimplemented)
#	event (WheelEvent) : The event representing the wheel operation
gview.wheel_event(event)

# A method invoked when a mouse press event occurs in the widget (to be reimplemented)
#	event (MouseEvent) : The event representing the press operation
gview.mouse_press_event(event)

# A method invoked when a mouse move event occurs in the widget (to be reimplemented)
#	event (MouseEvent) : The event representing the press operation
gview.mouse_move_event(event)

# A method invoked when a mouse release event occurs in the widget (to be reimplemented)
#	event (MouseEvent) : The event representing the press operation
gview.mouse_release_event(event)

# A method invoked when a background draw is requested (to be reimplemented)
#	painter (Painter) : A the toolkit dependent handle drawing
#	rect (Rect) : A rect showing the area of interest
gview.draw_background(painter, rect)

# Return the items at the given position
#	args () :
#	kwargs () :
# -> () :
item = gview.get_item_at(*args, **kwargs)

# Fit this item into the view
#	item () :
gview.fit_in_view(item)

# Center on the given item or point
#	item () :
item = gview.center_on(item)

# Translate the view by the given x and y pixels
#	x () :
#	y () :
# -> () :
item = gview.translate_view(x=0, y=0)

# Scale the view by the given x and y factors
#	x () :
#	y () :
# -> () :
item = gview.scale_view(x=1, y=1)

# Roteate the view by the given x and y factors.
#	angle () :
# -> () :
igview.rotate_view(angle=0)

# Reset all view transformations
gview.reset_view()

# Returns the scene coordinate point mapped to viewport coordinates
#	point () :
# -> () :
item = gview.map_from_scene(point)

# Returns the viewport coordinate point mapped to scene coordinates
#	point () :
# -> () :
item = gview.map_to_scene(point)

# Returns the size of a pixel in sceen coordinates
# -> () :
item = gview.pixel_density()

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsItem

from enamlx.widgets.api import GraphicsItem

	GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

#
# << (ToolkitObject) :
gitem = GraphicsItem()

# <-> (Typed(ProxyGraphicsItem)) : Proxy reference
proxy = gitem.proxy = proxy

# <-> (PointMember()) : Position
position = gitem.position = position

# <-> (Float(strict=False)) : Item rotation
rotation = gitem.rotation = rotation

# <-> (Float(1.0, strict=False)) : Item scale
scale = gitem.scale = scale

# <-> (Float(1.0, strict=False)) : Item opacity
opacity = gitem.opacity = opacity

# <-> (Bool()) : Item selected
selected = gitem.selected = selected

# <-> (Bool(True)) : Item is enabled
enabled = gitem.enabled = enabled

# <-> (Bool(True)) : Item is visible
visible = gitem.visible = visible

# <-> (Str()) : Tool tip
tool_tip = gitem.tool_tip = tool_tip

# <-> (Str()) : Status tip
status_tip = gitem.status_tip = status_tip

# <-> (Coerced(Feature.Flags)) : Set the extra features to enable for this widget
features = gitem.features = features

# <-> (Coerced(GraphicFeature.Flags)) : Set the extra features to enable for this widget
extra_features = gitem.extra_features = extra_features

# <-> (Event()) : Update
request_update = gitem.request_update = request_update

# <-> (Bool()) : Set whether this item can be selected
selectable = gitem.selectable = selectable

# <-> (Bool()) : Set whether this item can be moved
movable = gitem.movable = movable

# Ensure the widget is shown
gitem.show()

# Ensure the widget is hidden
gitem.hide()

# Set the keyboard input focus to this widget (DON'T)
gitem.set_focus()

# Clear the keyboard input focus from this widget (DON'T)
gitem.clear_focus()

# Test whether this widget has input focus (DON'T)
# -> (bool) :
#		True : if this widget has input focus
#		False : otherwise
focused = gitem.has_focus()

# A method invoked when the widget gains input focus (to be reimplemented)
gitem.focus_gained()

# A method invoked when the widget loses input focus (to be reimplemented)
gitem.focus_lost()

# A method called at the start of a drag-drop operation (to be reimplemented)
# -> (DragData) : An Enaml DragData object which holds the drag data
gitem.drag_start()

# A method called at the end of a drag-drop operation (to be reimplemented)
#	drag_data (DragData) : The drag data created by the `drag_start` method
#	result (DropAction) : The requested drop action when the drop completed
gitem.drag_end(drag_data, result)

# A method invoked when a drag operation enters the widget (to be reimplemented)
#	event (DropEvent) : The event representing the drag-drop operation
gitem.drag_enter(event)

# A method invoked when a drag operation moves in the widget (to be reimplemented)
#	event (DropEvent) : The event representing the drag-drop operation
gitem.drag_move(event)

# A method invoked when a drag operation leaves the widget (to be reimplemented)
gitem.drag_leave()

# A method invoked when the user drops the data on the widget (to be reimplemented)
#	event (DropEvent) : The event representing the drag-drop operation
gitem.drop(event)

# A method invoked when a mouse press event occurs in the widget (to be reimplemented)
#	event (MouseEvent) : The event representing the press operation
gitem.mouse_press_event(event)

# A method invoked when a mouse move event occurs in the widget (to be reimplemented)
#	event (MouseEvent) : The event representing the press operation
gitem.mouse_move_event(event)

# A method invoked when a mouse release event occurs in the widget (to be reimplemented)
#	event (MouseEvent) : The event representing the press operation
gitem.mouse_release_event(event)

# A method invoked when a wheel event occurs in the widget (to be reimplemented)
#	event (WheelEvent) : The event representing the wheel operation
gitem.wheel_event(event)

# A method invoked when this widget needs to be drawn (to be reimplemented)
#	painter (Object) : The toolkit dependent painter object
#	options (Object) : The toolkit dependent options object
#	widget (Widget) : The underlying widget
gitem.draw(painter, options, widget)

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : AbstractGraphicsShapeItem

from enamlx.widgets.graphics_view import AbstractGraphicsShapeItem

	AbstractGraphicsShapeItem:
		proxy = Typed(ProxyAbstractGraphicsShapeItem)
		pen = Instance(Pen)
		brush = Instance(Brush)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

# A common base for all path items
# << (GraphicsItem) :
agsitem = AbstractGraphicsShapeItem()

# <-> (Typed(ProxyAbstractGraphicsShapeItem)) : Proxy reference
proxy = agsitem.proxy = proxy

# <-> (Instance(Pen)) : Set the pen or "line" style
pen = agsitem.pen = pen

# <-> (Instance(Brush)) : Set the brush or "fill" style
brush = agsitem.brush = brush

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsRectItem

from enamlx.widgets.api import GraphicsRectItem

	GraphicsRectItem:
		proxy = Typed(ProxyGraphicsRectItem)
		width = Float(10.0, strict=False)
		height = Float(10.0, strict=False)
			#AbstractGraphicsShapeItem:
		proxy = Typed(ProxyAbstractGraphicsShapeItem)
		pen = Instance(Pen)
		brush = Instance(Brush)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

#
# << (AbstractGraphicsShapeItem) :
grectitem = GraphicsRectItem()

# <-> (Typed(ProxyGraphicsRectItem)) : Proxy reference
proxy = grectitem.proxy = proxy

# <-> (Float(10.0, strict=False)) : Width
width = grectitem.width = width

# <-> (Float(10.0, strict=False)) : Height
height = grectitem.height = height

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsEllipseItem

from enamlx.widgets.api import GraphicsEllipseItem

	GraphicsEllipseItem:
		proxy = Typed(ProxyGraphicsEllipseItem)
		width = Float(10.0, strict=False)
		height = Float(10.0, strict=False)
		span_angle = Float(360.0, strict=False)
		start_angle = Float(0.0, strict=False)
			#AbstractGraphicsShapeItem:
		proxy = Typed(ProxyAbstractGraphicsShapeItem)
		pen = Instance(Pen)
		brush = Instance(Brush)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

#
# << (AbstractGraphicsShapeItem) :
gelpsitem = GraphicsEllipseItem()

# <-> (Typed(ProxyGraphicsEllipseItem)) : Proxy reference
proxy = gelpsitem.proxy = proxy

# <-> (Float(10.0, strict=False)) : Width
width = gelpsitem.width = width

# <-> (Float(10.0, strict=False)) : Height
height = gelpsitem.height = height

# <-> (Float(360.0, strict=False)) : Sets the span angle for an ellipse segment to angle
span_angle = gelpsitem.span_angle = span_angle

# <-> (Float(0.0, strict=False)) : Sets the start angle for an ellipse segment to angle
start_angle = gelpsitem.start_angle = start_angle

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsPathItem

from enamlx.widgets.api import GraphicsPathItem

	GraphicsPathItem:
		proxy = Typed(ProxyGraphicsPathItem)
		path = Value()
			#AbstractGraphicsShapeItem:
		proxy = Typed(ProxyAbstractGraphicsShapeItem)
		pen = Instance(Pen)
		brush = Instance(Brush)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

#
# << (AbstractGraphicsShapeItem) :
gpitem = GraphicsPathItem()

# <-> (Typed(ProxyGraphicsPathItem)) : Proxy reference
proxy = gpitem.proxy = proxy

# <-> (Value()) : Path
path = gpitem.path = path

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsLineItem

from enamlx.widgets.api import GraphicsLineItem

	GraphicsLineItem:
		proxy = Typed(ProxyGraphicsLineItem)
		point = List(PointMember())
			#AbstractGraphicsShapeItem:
		proxy = Typed(ProxyAbstractGraphicsShapeItem)
		pen = Instance(Pen)
		brush = Instance(Brush)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

#
# << (AbstractGraphicsShapeItem) :
glinitem = GraphicsLineItem()

# <-> (Typed(ProxyGraphicsLineItem)) : Proxy reference
proxy = glinitem.proxy = proxy

# <-> (List(PointMember())) : An x,y or x,y,z point
point = glinitem.point = point

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsTextItem

from enamlx.widgets.api import GraphicsTextItem

	GraphicsTextItem:
		proxy = Typed(ProxyGraphicsTextItem)
		text = Str()
		font = FontMember()
			#AbstractGraphicsShapeItem:
		proxy = Typed(ProxyAbstractGraphicsShapeItem)
		pen = Instance(Pen)
		brush = Instance(Brush)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

#
# << (AbstractGraphicsShapeItem) :
gtextitem = GraphicsTextItem()

# <-> (Typed(ProxyGraphicsTextItem)) : Proxy reference
proxy = gtextitem.proxy = proxy

# <-> (Str()) : Text
text = gtextitem.text = text

# <-> (FontMember()) : Font
font = gtextitem.font = font

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsPolygonItem

from enamlx.widgets.api import GraphicsPolygonItem

	GraphicsPolygonItem:
		proxy = Typed(ProxyGraphicsPolygonItem)
		points = List(PointMember())
			#AbstractGraphicsShapeItem:
		proxy = Typed(ProxyAbstractGraphicsShapeItem)
		pen = Instance(Pen)
		brush = Instance(Brush)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

#
# << (AbstractGraphicsShapeItem) :
gpolitem = GraphicsPolygonItem()

# <-> (Typed(ProxyGraphicsPolygonItem)) : Proxy reference
proxy = gpolitem.proxy = proxy

# <-> (List(PointMember())) : A list of (x,y) or (x,y,z) points
points = gpolitem.points = points

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsImageItem

from enamlx.widgets.api import GraphicsImageItem

	GraphicsImageItem:
		proxy = Typed(ProxyGraphicsImageItem)
		image = Instance(Image)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

#
# << (GraphicsItem) :
giitem = GraphicsImageItem()

# <-> (Typed(ProxyGraphicsImageItem)) : Proxy reference
proxy = giitem.proxy = proxy

# <-> (Instance(Image)) : Image
image = giitem.image = image

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsItemGroup

from enamlx.widgets.api import GraphicsItemGroup

	GraphicsItemGroup:
		proxy = Typed(ProxyGraphicsItemGroup)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

# A common base for all path items
# << (GraphicsItem) :
gigroup = GraphicsItemGroup()

# <-> (Typed(ProxyGraphicsItemGroup)) : Proxy reference
proxy = gigroup.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : GraphicsWidget

from enamlx.widgets.api import GraphicsWidget

	GraphicsWidget:
		proxy = Typed(ProxyGraphicsWidget)
			#GraphicsItem:
		proxy = Typed(ProxyGraphicsItem)
		position = PointMember()
		rotation = Float(strict=False)
		scale = Float(1.0, strict=False)
		opacity = Float(1.0, strict=False)
		selected = Bool()
		enabled = Bool(True)
		visible = Bool(True)
		tool_tip = Str()
		status_tip = Str()
		features = Coerced(Feature.Flags)
		extra_features = Coerced(GraphicFeature.Flags)
		request_update :: Event()
		selectable = Bool()
		movable = Bool()
		#
		self.show()
		self.hide()
		#
		focus_gained => ():
		focus_lost => ():
		drag_start => ():
		drag_end => (drag_data, result):
		drag_enter => (event):
		drag_move => (event):
		drag_leave => ():
		drop => (event):
		mouse_press_event => (event):
		mouse_move_event => (event):
		mouse_release_event => (event):
		wheel_event => (event):
		draw => (painter, options, widget):
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

# Use this to embed a widget within a graphics scene
# << (GraphicsItem) :
gwidget = GraphicsWidget()

# <-> (Typed(ProxyGraphicsWidget)) : Proxy reference
proxy = gwidget.proxy = proxy

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : Pen

from enamlx.widgets.api import Pen

	Pen:
		color = ColorMember()
		width = Float(1.0, strict=False)
		line_style = Enum('solid', 'dash', 'dot', 'dash_dot', 'dash_dot_dot', 'custom', 'none')
		cap_style = Enum('square', 'flat', 'round')
		join_style = Enum('bevel', 'miter', 'round')
		dash_pattern = List(Float(strict=False))
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

#
# << (Atom) :
pen = Pen()

# <-> (ColorMember()) : Color
color = pen.color = color

# <-> (Float(1.0, strict=False)) : Width
width = pen.width = width

# <-> (Enum('solid', 'dash', 'dot', 'dash_dot', 'dash_dot_dot', 'custom', 'none')) : Line Style
line_style = pen.line_style = line_style

# <-> (Enum('square', 'flat', 'round')) : Cap Style
cap_style = pen.cap_style = cap_style

# <-> (Enum('bevel', 'miter', 'round')) : Join Style
join_style = pen.join_style = join_style

# <-> (List(Float(strict=False))) : Dash pattern used when line_style is 'custom'
dash_pattern = pen.dash_pattern = dash_pattern

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : Brush

from enamlx.widgets.api import Brush

	Brush:
		color = ColorMember()
		image = Instance(Image)
		style = Enum('solid', 'dense1', 'dense2', 'dense3', 'dense4', 'dense5', 'dense6', 'dense7', 'horizontal', 'vertical', 'cross', 'diag', 'bdiag', 'fdiag', 'linear', 'radial', 'conical', 'texture', 'none')
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

#
# << (Atom) :
brsh = Brush()

# <-> (ColorMember()) : Color
color = brsh.color = color

# <-> (Instance(Image)) : image
image = brsh.image = image

# <-> (Enum('solid', 'dense1', 'dense2', 'dense3', 'dense4', 'dense5', 'dense6', 'dense7', 'horizontal', 'vertical', 'cross', 'diag', 'bdiag', 'fdiag', 'linear', 'radial', 'conical', 'texture', 'none')) : Style
style = brsh.style = style

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : Point

from enamlx.widgets.api import Point

	Point:
		x = Float(0, strict=False)
		y = Float(0, strict=False)
		z = Float(0, strict=False)
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

#
# << (Atom) :
pt = Point()

# <-> (Float(0, strict=False)) : x position
x = pt.x = x

# <-> (Float(0, strict=False)) : y position
y = pt.y = y

# <-> (Float(0, strict=False)) : z position
z = pt.z = z

pt.__init__
pt.__iter__
pt.__len__
pt.__eq__
pt.__add__
pt.__radd__
pt.__sub__
pt.__rsub__
pt.__mul__
pt.__rmul__
pt.__div__
pt.__rdiv__
pt.__neg__
pt.__hash__
pt.__getitem__
pt.__repr__

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# EnamlX : Rect

from enamlx.widgets.api import Rect

	Rect:
		x = Float(0, strict=False)
		y = Float(0, strict=False)
		width = Float(0, strict=False)
		height = Float(0, strict=False)
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

#
# << (Atom) :
rct = Rect()

# <-> (Float(0, strict=False)) :
x = rct.x = x

# <-> (Float(0, strict=False)) :
y = rct.y = y

# <-> (Float(0, strict=False)) :
width = rct.width = width

# <-> (Float(0, strict=False)) :
height = rct.height = height

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
