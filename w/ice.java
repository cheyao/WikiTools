package com.cyao.theconverter.worlds;

import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.Regex;

@Metadata(mo3720d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004J\u0006\u0010\u0007\u001a\u00020\u0003R\u0011\u0010\u0002\u001a\u00020\u0003¢\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006¨\u0006\b"}, mo3721d2 = {"Lcom/cyao/theconverter/worlds/ice;", "", "last", "", "(Ljava/lang/String;)V", "getLast", "()Ljava/lang/String;", "ice1", "app_debug"}, mo3722k = 1, mo3723mv = {1, 6, 0}, mo3725xi = 48)
/* compiled from: ice.kt */
public final class ice {
    private final String last;

    public ice(String last2) {
        Intrinsics.checkNotNullParameter(last2, "last");
        this.last = last2;
    }

    public final String getLast() {
        return this.last;
    }

    public final String ice1() {
        Regex regex = new Regex("\\s*\\(iceage" + "@ZombieTypes" + "\\)\\s*");
        Regex regex2 = new Regex("\\s*\\(iceage_armor1" + "@ZombieTypes" + "\\)\\s*");
        Regex regex3 = new Regex("\\s*\\(iceage_armor2" + "@ZombieTypes" + "\\)\\s*");
        Regex regex4 = new Regex("\\s*\\(iceage_armor3" + "@ZombieTypes" + "\\)\\s*");
        Regex regex5 = new Regex("\\s*\\(iceage_hunter" + "@ZombieTypes" + "\\)\\s*");
        Regex regex6 = new Regex("\\s*\\(iceage_dodo" + "@ZombieTypes" + "\\)\\s*");
        Regex regex7 = new Regex("\\s*\\(iceage_troglobite_1block" + "@ZombieTypes" + "\\)\\s*");
        Regex regex8 = new Regex("\\s*\\(iceage_troglobite_2block" + "@ZombieTypes" + "\\)\\s*");
        Regex regex9 = new Regex("\\s*\\(iceage_troglobite" + "@ZombieTypes" + "\\)\\s*");
        Regex regex10 = new Regex("\\s*\\(iceage_weaselhoarder" + "@ZombieTypes" + "\\)\\s*");
        Regex regex11 = new Regex("\\s*\\(iceage_weasel" + "@ZombieTypes" + "\\)\\s*");
        Regex regex12 = new Regex("\\s*\\(iceage_gargantuar" + "@ZombieTypes" + "\\)\\s*");
        Regex regex13 = new Regex("\\s*\\(iceage_imp" + "@ZombieTypes" + "\\)\\s*");
        return new Regex("\\s*\\(hellbird" + "@ZombieTypes" + "\\)\\s*").replace((CharSequence) regex13.replace((CharSequence) regex12.replace((CharSequence) regex11.replace((CharSequence) regex10.replace((CharSequence) regex9.replace((CharSequence) regex8.replace((CharSequence) regex7.replace((CharSequence) regex6.replace((CharSequence) regex5.replace((CharSequence) regex4.replace((CharSequence) regex3.replace((CharSequence) regex2.replace((CharSequence) regex.replace((CharSequence) this.last, "58 \\{\\{Cave Zombie|2}}"), "59 \\{\\{Cave Conehead Zombie|2}}"), "60 \\{\\{Cave Buckethead Zombie|2}}"), "61 \\{\\{Blockhead Zombie|2}}"), "65 \\{\\{Hunter Zombie|2}}"), "64 \\{\\{Dodo Rider Zombie|2}}"), "66 \\{\\{Troglobite|2}}"), "66 \\{\\{Troglobite|2}}"), "66 \\{\\{Troglobite|2}}"), "67 \\{\\{Weasel Hoarder|2}}"), "68 \\{\\{Ice Weasel|2}}"), "62 \\{\\{Sloth Gargantuar|2}}"), "63 \\{\\{Yeti Imp|2}}"), "69 \\{\\{Zombie Nether Dodo|2}}");
    }
}
