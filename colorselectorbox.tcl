#############################################################################
# Generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#  Nov 09, 2020 08:02:51 PM CET  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { \
    kvitt_svart_png "./asset/graphics/system_icon/kvitt_svart.png" \
    snu_farge_png "./asset/graphics/system_icon/snu_farge.png" \
}
vTcl:create_project_images $image_list   ;# In image.tcl


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 0
set vTcl(mode) Absolute
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 111x112+954+383
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1905 1050
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra51 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 105 -highlightcolor black -width 105 
    vTcl:DefineAlias "$top.fra51" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra51
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background LightSkyBlue1 -borderwidth 2 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief raised 
    vTcl:DefineAlias "$site_3_0.lab52" "lbl_bottom_color" vTcl:WidgetProc "Toplevel1" 1
    bind $site_3_0.lab52 <ButtonRelease-1> {
        lambda e: on_lbl_bottom_color(e)
    }
    label $site_3_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background cornflowerblue -borderwidth 2 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief raised 
    vTcl:DefineAlias "$site_3_0.lab53" "lbl_top_color" vTcl:WidgetProc "Toplevel1" 1
    bind $site_3_0.lab53 <ButtonRelease-1> {
        lambda e: on_lbl_top_color(e)
    }
    button $site_3_0.but54 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -image kvitt_svart_png 
    vTcl:DefineAlias "$site_3_0.but54" "btn_black_white" vTcl:WidgetProc "Toplevel1" 1
    bind $site_3_0.but54 <ButtonRelease-1> {
        lambda e: on_btn_black_white(e)
    }
    button $site_3_0.but55 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command on_btn_change_color \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -image snu_farge_png -text Button 
    vTcl:DefineAlias "$site_3_0.but55" "btn_change_color" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab52 \
        -in $site_3_0 -x 41 -y 41 -width 60 -relwidth 0 -height 60 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 0 -y 0 -width 60 -height 60 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but54 \
        -in $site_3_0 -x 1 -y 61 -width 41 -relwidth 0 -height 41 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but55 \
        -in $site_3_0 -x 60 -y 2 -width 41 -relwidth 0 -height 41 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra51 \
        -in $top -x 5 -y 5 -width 105 -relwidth 0 -height 105 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

