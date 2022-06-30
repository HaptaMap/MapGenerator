/*difference () {
    cube([240, 240, 10]);
    #translate([-10,-10,0.2]) color([0,1,0]) linear_extrude(height=10) scale([1,1, 1]) import("test_map.dxf");
}*/
union() {
    // 100 dots per inch, with 12 inch size -> 1200 dots
    // Openscad makes each dot 1mm, so if we want this to be 200mm/200mm
    // it must be 200 dpi / 1200 dots -> 1/6 the size
    scale([1/6,1/6,0.07]) surface(file = "test_map.png");
    translate([0, 0, 0]) cube([100,100,0.7]);
    translate([90,99.9,0]) cube([10,10,2]);
}