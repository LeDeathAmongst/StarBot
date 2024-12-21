pico-8 cartridge // http://www.pico-8.com
version 41
__lua__
function _init()
	flip()
	--1 is 8x8, 2 is 16x16, etc
	anim_size=3
	--line down the spritesheet
	--that we're drawing
	anim=1
	--fast or slow animation
	fast=false
	--how many frames
	--the animation has
	anim_length=4
end
t=-1
function _draw()
	if t==0 then
		extcmd("rec")
	end
	cls()
	spd = 5
	if fast then
		spd = 3
	end
	a=anim-1
	--fixes single frame starting frame
	it = flr(max(t,0)/spd)%(anim_length+1)
	i = it*anim_size + a*16*anim_size + 1
	spr(i,0,0,anim_size,anim_size)
	t += 1
	if it==anim_length and t>0 then
		flip()
		extcmd("video")
		_draw = function()end
	end
end
-- gifsicle --colors=33 --crop=0,0+96x96 a.gif > at.gif                
-- gifsicle --colors=33 at.gif -w | gifsicle -U --disposal=previous -t="0,0,0" -O3 > output.gif
__gfx__
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00700700000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00077000000000000111111110000000000000000000000000000000000000000000000000000000000000000111111110000000000000000000000000000000
00077000000000001111111111000000000000000111111110000000000000000111111110000000000000001111111111000000000000000000000000000000
00700700000000011111111111000000000000001111111111000000000000001111111111000000000000011111111111000000000000000000000000000000
00000000000000012211122111100000000000011111111111000000000000011111111111000000000050012211122111100000000000000000000000000000
00000000000000011111111111100000000000012211122111100000000000012211122111100000000000011111111111100000000000000000000000000000
00000000000000011111111111110000000000011111111111100000000000011111111111100000000000011111111111110000000000000000000000000000
00000000000500011111111111110000000000011111111111110000000000011111111111110000000000011111111111110000000000000000000000000000
00000000000000001111111111110000000000011111111111110000000000011111111111110000000000001111111111110000000000000000000000000000
0000000000000000011111111dd1000000000000111111111dd1000000000000111111111111000000000000011111111dd10000000000000000000000000000
0000000000000000111111111ddd000000000000011111111ddd000000000a00011111111dd1000000400000111111111dd10000000000000000000000000000
000000000000051111111111111d00000000051111111111111dd00000000000111111111dd10000000005114111111111d10000000000000000000000000000
000000000000555001111111111d000000005550111111111111d0000a0009111a11111111d10000000059500111111111d10000000000000000000000000000
0000000000055955011111111add000000055955011111111a1dd000000099500111111111d10000000559950111111a1dd10000000000000000000000000000
000000000005959501111111add10000000595850111111111dd00000005999501111111add100000005858501111111dd110000000000000000000000000000
0000000000058585011111111a11000000058585011111111a1a000000a58598a111111add110000000585850111111a1a110000000000000000000000000000
000000000005585501110011111100000005585501111111111100000005858501111111a1110000000558550111111100110000000000000000000000000000
00000000000055500011000000110000000055500111110011110000000558550111111100110000000055500011001100000000000000000000000000000000
00000000000000000000000000000000000000000100110000000000000055500011001100000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000111111110000000000000000000000000000000000000000000000000000000000000000111111110000000000000000000000000000000
00000000000000001111111111000000000000000111111110000000000000000111111110000000000000001111111111000000000000000000000000000000
00000000000000011111111111000000000000001111111111000000000000001111111111000000000000011111111111000000000000000000000000000000
00000000000000015511155111100000000000011111111111000000000000011111111111000000000000015511155111100000000000000000000000000000
00000000000000011111111111100000000000015511155111100000000000015511155111100000000000011111111111100000000000000000000000000000
000000000000000111111dd11111000000000001111111dd11100000000000011111111111100000000000011111111111110000000000000000000000000000
000000000000000111111ddd1111000000000001111111dd1111000000000001111111dd111100000000000111111dd111110000000000000000000000000000
00000000000000001111111dddd10000000000011111111dd111000000000001111111dd111100000000000011111ddd11110000000000000000000000000000
0000000000000000011166111dd100000000000011111661ddd10000000000001111111dd1110000000000000111611dddd10000000000000000000000000000
0000000000000000111656661111000000000000011116661dd100000000000001116611ddd1000000000000111656611dd10000000000000000000000000000
0000000000000511111665666111000000000511111116661111000000000000111166611dd10000000005111116656611110000000000000000000000000000
00000000000055500166566611110000000055501111656611110000000005111111165111110000000055500116566111110000000000000000000000000000
00000000000559550116656111110000000559550111666111110000000055500111166111110000000559550116656111110000000000000000000000000000
00000000000595950111661111110000000595850111111111110000000559550111116111110000000585950111166111110000000000000000000000000000
00000000000585850111111111110000000585850111111111110000000585950111111111110000000585850111111111110000000000000000000000000000
00000000000558550111001111110000000558550111111111110000000585850111111111110000000558550111111100110000000000000000000000000000
00000000000055500011000000110000000055500111110011110000000558550111111100110000000055500011001100000000000000000000000000000000
00000000000000000000000000000000000000000100110000000000000055500011001100000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001100000000000000000000000000000000000
00000000000000000001000000000000000000000000000000000000000000000000000000000000000000000011000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000110000000000000000000000010000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000001100000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000011100000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000011000000000000000000000010000000000000000000000000000000000000000
00000000000000000000000000000000000000000001100000000000000000011000000000000000000000100000000000000000000000000000000000000000
00000000000000000000000000000000000000000011111000000000000000011100000000000000000000100000000000000000000000000000000000000000
00000000000000000000000000000000000000000011111100000000000000001100000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000001111110000000000000001100000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000001110000000000001000110000000000000000000000000000000000000000000000000000000000000
00000000000000000000011100000000000000000000001110000000000000100011000000000000000000000000000000000000000000000000000000000000
00000000000000000000011110000000000000000000011110000000000000100011000000000000000000000000000000000000000000000000000000000000
00000000000000000000111100000000000000000000011000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000001110000000000000000001100111110000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000001111000000000000000000100111110000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000011111000000000000000000000011100000000000000000000000000000000000000000011111000000000000000000000000000000000
00000000000000000055551100000000000000000055550000000000000000000055550000000000000000000155551100000000000000000000000000000000
00000000000000000551155100000000000000000550055000000000000000000550055000000000000000000551155100000000000000000000000000000000
00000000000000005505515000000000000000005505505000000000000000005505505000000000000000005515515000000000000000000000000000000000
0000000000000000055dd5500000000000000000055dd5500000000000000000055dda500000000000000000055dd55000000000000000000000000000000000
00000000000000000055550000000000000000000055550000000000000000000055550000000000000000000055550000000000000000000000000000000000
00000000000000000000000500000000000000000000000000000000000000000000000000000000000000000000000400000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0000000000000000000000000000000000000
0000000000000000000000000000000000000000000c00000000000000000000000c0000000000000000000000c0000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000cc0000000000000000000000000000000000000000000000000000000000
0000000000000000011c1111100000000000000000000000000000000000000000000c0000000000000000000111111110000000000000000000000000000000
000000000000000011111111110000000000000001111c1110000000000000000111111110000000000000001111111111000000000000000000000000000000
00000000000000011111111111000000000000001111cc1111000000000000001111111111000000000000011111c11111000000000000000000000000000000
00000000000000015c1115511110000000000001111cc1111100000000000001111111111100000000000001551c155111100000000000000000000000000000
00000000000000011cc1111111100000000000015511155111100000000000015511155111100000000000011171111111100000000000000000000000000000
0000000000000001111117111111000000000001111111111110000000000001111c111111100000000000011117111111110000000000000000000000000000
00000000000000011111711111110000000000011111111111110000000000011971717911110000000000019771177911110000000000000000000000000000
00000000000000009777177911110000000000011191794111110000000000011197179441110000000000001997799441110000000000000000000000000000
0000000000000000097799944dd1000000000000119779441dd1000000000000119779441111000000000000011994441dd10000000000000000000000000000
0000000000000000119944411dd1000000000000019794411dd1000000000000011994411dd1000000000000111144111dd10000000000000000000000000000
0000000000000511111441111dd10000000005111119944111d1000000000000111144111dd10000000005111111111111d10000000000000000000000000000
000000000000555001111111dd11000000005550111144111dd10000000005111111111111d100000000555001111a111dd10000000000000000000000000000
000000000005595501111a1dd111000000055955011111111d11000000005550011111111dd10000000559550111addddd110000000000000000000000000000
00000000000595950111addd11110000000595850111adddd11100000005595501111a11dd1100000005859501111a1111110000000000000000000000000000
000000000005858501111a11111100000005858501111a1111110000000585950111adddd1110000000585850111111111110000000000000000000000000000
000000000005585501110011111100000005585501111111111100000005858501111a1111110000000558550111111100110000000000000000000000000000
00000000000055500011000000110000000055500111110011110000000558550111111100110000000055500011001100000000000000000000000000000000
00000000000000000000000000000000000000000100110000000000000055500011001100000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
000000000000c000000000000000000000000000000000000000000000c000000c00c00000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000cc0000cc00000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000c00000000000000000000000c000cc00000000000000000c000000000000000000000000000000000000000000000
00000000000000000111111110000000000c00000000000000000000000cc00c0000000000000000000000000111111110000000000000000000000000000000
0000000000000022111111111122000000cc00cc01111111100000000000c0000111111110000000000c00221111111111006600000000000000000000000000
0000000000000221666611dd1122200000c060c011c1111116200000000000001111111111600000000c062111111111110006d0000000000000000000000000
0000000000c000215566665dd11dd00000ccd0c111cc11166550dd00000000c1651111116656000000000601551115511110ddd0000000000000000000000000
00000000cc0000211111666d111dd0000cccd0cc551c15565555dd0000000c0655111551656660000000066111c111111110dd00000000000000000000000000
00000000cc00000111166661d111d0000cccd00cc111111555550d0000000cc5555111116656d0000000056611cc111111116d00000000000000000000000000
00000000cc00000c1c6611ddd111d0000cc0d00c1c11111555510d00000000c5551111111661d00000000661111c111111110d00000000000000000000000000
00000000ccc0000cc6611111111dd0000ccc600c11111111111ddd00000000c1111111111111d0000000060cc11c11111111dd00000000000000000000000000
00000000ccc00000c111111111dd000000cc0c001111111111dd00000000000011111111111dd00000c00000c111111111ddd000000000000000000000000000
000000000cc00000c11111111111000000c000c0011111111111000000000000011c111111dd000000c0000cc111111111110000000000000000000000000000
000000000cc0051cc11111111111000000000cc1111111111111000000000000111c1111111100000cc0051c1111111111110000000000000000000000000000
000000000c00555c011111111111000000005c50111111111111000000000511111c1111111100000c00555c0111111111110000000000000000000000000000
000000000c0c5c55011111111111000000055c5501c111111111000000c0555c01c11111111100000ccc5c550111111111110000000000000000000000000000
000000000cccc5c501111111111100000005c5c5cc1111111111000000c55c550cc11111111100000cccc5c50111111111110000000000000000000000000000
0000000000ccc5c501111111111100000005c5cccc1111111111000000c5c5c50c1111111111000000ccc5c50111111111110000000000000000000000000000
000000000005cc55011100111111000000055ccc011111111111000000ccc5c5011111111111000000055c550111111100110000000000000000000000000000
0000000000005550001100000011000000005550011111001111000000055c550111111100110000000055500011001100000000000000000000000000000000
00000000000000000000000000000000000000000100110000000000000055500011001100000000000000000000000000000000000000000000000000000000
