package com.cyao.theconverter.worlds;

import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.Regex;

@Metadata(mo3720d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004J\u0006\u0010\u0007\u001a\u00020\u0003R\u0011\u0010\u0002\u001a\u00020\u0003¢\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006¨\u0006\b"}, mo3721d2 = {"Lcom/cyao/theconverter/worlds/neon;", "", "last", "", "(Ljava/lang/String;)V", "getLast", "()Ljava/lang/String;", "neon1", "app_debug"}, mo3722k = 1, mo3723mv = {1, 6, 0}, mo3725xi = 48)
/* compiled from: neon.kt */
public final class neon {
    private final String last;

    public neon(String last2) {
        Intrinsics.checkNotNullParameter(last2, "last");
        this.last = last2;
    }

    public final String getLast() {
        return this.last;
    }

    public final String neon1() {
        Regex regex = new Regex("\\s*\\(eighties" + "@ZombieTypes" + "\\)\\s*");
        Regex regex2 = new Regex("\\s*\\(eighties_armor1" + "@ZombieTypes" + "\\)\\s*");
        Regex regex3 = new Regex("\\s*\\(eighties_armor2" + "@ZombieTypes" + "\\)\\s*");
        Regex regex4 = new Regex("\\s*\\(eighties_punk" + "@ZombieTypes" + "\\)\\s*");
        Regex regex5 = new Regex("\\s*\\(eighties_glitter" + "@ZombieTypes" + "\\)\\s*");
        Regex regex6 = new Regex("\\s*\\(eighties_mc" + "@ZombieTypes" + "\\)\\s*");
        Regex regex7 = new Regex("\\s*\\(eighties_breakdancer" + "@ZombieTypes" + "\\)\\s*");
        Regex regex8 = new Regex("\\s*\\(eighties_arcade" + "@ZombieTypes" + "\\)\\s*");
        Regex regex9 = new Regex("\\s*\\(eighties_8bit" + "@ZombieTypes" + "\\)\\s*");
        Regex regex10 = new Regex("\\s*\\(eighties_8bit_armor1" + "@ZombieTypes" + "\\)\\s*");
        Regex regex11 = new Regex("\\s*\\(eighties_8bit_armor2" + "@ZombieTypes" + "\\)\\s*");
        Regex regex12 = new Regex("\\s*\\(eighties_boombox" + "@ZombieTypes" + "\\)\\s*");
        Regex regex13 = new Regex("\\s*\\(eighties_gargantuar" + "@ZombieTypes" + "\\)\\s*");
        Regex regex14 = new Regex("\\s*\\(eighties_imp" + "@ZombieTypes" + "\\)\\s*");
        return new Regex("\\s*\\(eighties_imp" + "@ZombieTypes" + "\\)\\s*").replace((CharSequence) regex14.replace((CharSequence) regex13.replace((CharSequence) regex12.replace((CharSequence) regex11.replace((CharSequence) regex10.replace((CharSequence) regex9.replace((CharSequence) regex8.replace((CharSequence) regex7.replace((CharSequence) regex6.replace((CharSequence) regex5.replace((CharSequence) regex4.replace((CharSequence) regex3.replace((CharSequence) regex2.replace((CharSequence) regex.replace((CharSequence) this.last, "116 \\{\\{P|Neon Zombie|2}}"), "117 \\{\\{P|Neon Conehead|2}}"), "118 \\{\\{P|Neon Buckethead|2}}"), "122 \\{\\{P|Punk Zombie|2}}"), "121 \\{\\{P|Glitter Zombie|2}}"), "124 \\{\\{P|MC Zom-B|2}}"), "129 \\{\\{P|Breakdancer Zombie|2}}"), "125 \\{\\{P|Arcade Zombie|2}}"), "126 \\{\\{P|8-Bit Zombie|2}}"), "127 \\{\\{P|8-Bit Conehead Zombie|2}}"), "128 \\{\\{P|8-Bit Buckethead Zombie|2}}"), "123 \\{\\{P|Boombox Zombie|2}}"), "119 \\{\\{P|Hair Metal Gargantuar|2}}"), "120 \\{\\{P|Impunk|2}}"), "130 \\{\\{P|Football Zombie|2}}");
    }
}
