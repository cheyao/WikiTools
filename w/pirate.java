package com.cyao.theconverter.worlds;

import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.Regex;

@Metadata(mo3720d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004J\u0006\u0010\u0007\u001a\u00020\u0003R\u0011\u0010\u0002\u001a\u00020\u0003¢\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006¨\u0006\b"}, mo3721d2 = {"Lcom/cyao/theconverter/worlds/pirate;", "", "last", "", "(Ljava/lang/String;)V", "getLast", "()Ljava/lang/String;", "pirate1", "app_debug"}, mo3722k = 1, mo3723mv = {1, 6, 0}, mo3725xi = 48)
/* compiled from: pirate.kt */
public final class pirate {
    private final String last;

    public pirate(String last2) {
        Intrinsics.checkNotNullParameter(last2, "last");
        this.last = last2;
    }

    public final String getLast() {
        return this.last;
    }

    public final String pirate1() {
        Regex regex = new Regex("\\s*\\(pirate" + "@ZombieTypes" + "\\)\\s*");
        Regex regex2 = new Regex("\\s*\\(pirate_armor1" + "@ZombieTypes" + "\\)\\s*");
        Regex regex3 = new Regex("\\s*\\(pirate_armor2" + "@ZombieTypes" + "\\)\\s*");
        Regex regex4 = new Regex("\\s*\\(pirate_armor4" + "@ZombieTypes" + "\\)\\s*");
        Regex regex5 = new Regex("\\s*\\(swashbuckler" + "@ZombieTypes" + "\\)\\s*");
        Regex regex6 = new Regex("\\s*\\(seagull" + "@ZombieTypes" + "\\)\\s*");
        Regex regex7 = new Regex("\\s*\\(pelican" + "@ZombieTypes" + "\\)\\s*");
        Regex regex8 = new Regex("\\s*\\(barrelroller" + "@ZombieTypes" + "\\)\\s*");
        Regex regex9 = new Regex("\\s*\\(pirate_barrel" + "@ZombieTypes" + "\\)\\s*");
        Regex regex10 = new Regex("\\s*\\(cannon" + "@ZombieTypes" + "\\)\\s*");
        Regex regex11 = new Regex("\\s*\\(pirate_captain" + "@ZombieTypes" + "\\)\\s*");
        Regex regex12 = new Regex("\\s*\\(pirate_gargantuar" + "@ZombieTypes" + "\\)\\s*");
        return new Regex("\\s*\\(pirate_imp" + "@ZombieTypes" + "\\)\\s*").replace((CharSequence) regex12.replace((CharSequence) regex11.replace((CharSequence) regex10.replace((CharSequence) regex9.replace((CharSequence) regex8.replace((CharSequence) regex7.replace((CharSequence) regex6.replace((CharSequence) regex5.replace((CharSequence) regex4.replace((CharSequence) regex3.replace((CharSequence) regex2.replace((CharSequence) regex.replace((CharSequence) this.last, "45 \\{\\{P|Pirate Zombie|2}}"), "46 \\{\\{P|Conehead Pirate|2}}"), "47 \\{\\{P|Buckethead Pirate|2}}"), "48\\{\\{P|Cannonhead Zombie|2}}"), "51 \\{\\{P|Swashbuckler Zombie|2}}"), "54 \\{\\{P|Seagull Zombie|2}}"), "57 \\{\\{P|Pelican Zombie|2}}"), "52 \\{\\{P|Barrel Roller Zombie|2}}"), "53 \\{\\{P|Pirate Barrel|2}}"), "56 \\{\\{P|Imp Cannon|2}}"), "55 \\{\\{P|Pirate Captain Zombie|2}}"), "49 \\{\\{P|Gargantuar Pirate|2}}"), "50 \\{\\{P|Imp Pirate Zombie|2}}");
    }
}
