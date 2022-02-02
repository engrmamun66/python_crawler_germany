:fromStart
@echo off
SET var=%cd%
color a
title GY Ad Crawer - V6.0
cls


echo.
echo         `:ydNMMMmhs-  hdmmmmmmmdy+.       hNNNNs      /mdddo  /ddddo  +dddmo :mmdddddddmd: -ddmmmmmmmhs/` 
 echo       /mMMMMMMMMMMM: NMMMMNNNMMMMM+     sMMMMMMo     oMMMMy  +MMMMy  oMMMMy :MMMMMNNNNMMo .MMMMMNNNMMMMN-
echo       /MMMMNs/::odm/  mMMMM-`.oMMMMN    /MMMMMMMM/    sMMMMs  +MMMMs  +MMMMh -MMMMN////++- `MMMMm``-hMMMMy
echo       dMMMM+     ``   dMMMM+//hMMMMy   -NMMMhhMMMN:   :NMMMd` hMMMMm``dMMMN/ .MMMMMNNNNMM. `MMMMN//+mMMMM+
echo       dMMMM+     ``   mMMMMMMMMMMN+`  `mMMMMooMMMMN.   /NMMMdoMMMMMMyhMMMN/  .MMMMMmmmmmm` `MMMMMMMMMMMd/ 
echo       /MMMMNy/:/odm/  NMMMM+/NMMMN:   hMMMMMMMMMMMMd`   :NMMMMMMNNMMMMMMN/   :MMMMN/////+: .MMMMN/oMMMMm. 
echo        /mMMMMMMMMMMN:`NMMMM: :MMMMN: sMMMMmhhhhmMMMMh    :NMMMMM+/MMMMMN:    /MMMMMMMMMMMm :MMMMM` oMMMMm.
echo         `:sdNMMNmho. `dmmmm/  /dmmmd-dmmmd.    -dmmmm-    -dmmd+  +dmmd:     :ddddddddmmmo -dmmmd.  sdmmmy

echo .
echo        ===============================                                    ================================
echo        =============================== Powerful Google And Youtube Crawer ================================
echo        ===============================                                    ================================
echo .

set /p startCon=  ------------- Start Crawl(y/n)?
if %startCon%==n (
    exit
)

:intial-step

echo.
set /p con=       Are you cofirm(y/n)?
if %con%==y (
     
echo   Crawl is starting...               
echo.
    @REM python operation start 
    python pc.py
    @REM dir /b
)

cls
echo.
echo.
echo ================= Powerful Google And Youtube Crawer =====================
Goto  fromStart

