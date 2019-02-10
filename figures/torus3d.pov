#include "colors.inc"
#include "shapes.inc"
#include "textures.inc"

camera { location <-5,11,-19>
	direction <4,4,4>
	look_at <0,1,0>
}

light_source { <1,15,-5> color White
	spotlight
	point_at <0,0,0>
	radius 5
	falloff 15
	tightness 10
}

object { torus { 1.5 , 0.5 }
	translate <0,1,0>
	pigment { color Gray }
	finish { phong 0.9 phong_size 100 reflection 0 ambient 0.2 diffuse 0.8 }
}
