package com.cyao.theconverter.worlds;

import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.Regex;

@Metadata(mo3720d1 = {"\u0000\u0012\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0005\u0018\u00002\u00020\u0001B\r\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0002\u0010\u0004J\u0006\u0010\u0007\u001a\u00020\u0003R\u0011\u0010\u0002\u001a\u00020\u0003¢\u0006\b\n\u0000\u001a\u0004\b\u0005\u0010\u0006¨\u0006\b"}, mo3721d2 = {"Lcom/cyao/theconverter/worlds/west;", "", "last", "", "(Ljava/lang/String;)V", "getLast", "()Ljava/lang/String;", "west1", "app_debug"}, mo3722k = 1, mo3723mv = {1, 6, 0}, mo3725xi = 48)
/* compiled from: west.kt */
public final class west {
    private final String last;

    public west(String last2) {
        Intrinsics.checkNotNullParameter(last2, "last");
        this.last = last2;
    }

    public final String getLast() {
        return this.last;
    }

    public final String west1() {
        Regex regex = new Regex("\\s*\\(cowboy" + "@ZombieTypes" + "\\)\\s*");
        Regex regex2 = new Regex("\\s*\\(cowboy_armor1" + "@ZombieTypes" + "\\)\\s*");
        Regex regex3 = new Regex("\\s*\\(cowboy_armor2" + "@ZombieTypes" + "\\)\\s*");
        Regex regex4 = new Regex("\\s*\\(cowboy_armor4" + "@ZombieTypes" + "\\)\\s*");
        Regex regex5 = new Regex("\\s*\\(prospector" + "@ZombieTypes" + "\\)\\s*");
        Regex regex6 = new Regex("\\s*\\(piano" + "@ZombieTypes" + "\\)\\s*");
        Regex regex7 = new Regex("\\s*\\(poncho" + "@ZombieTypes" + "\\)\\s*");
        Regex regex8 = new Regex("\\s*\\(poncho_no_plate" + "@ZombieTypes" + "\\)\\s*");
        Regex regex9 = new Regex("\\s*\\(poncho_plate" + "@ZombieTypes" + "\\)\\s*");
        Regex regex10 = new Regex("\\s*\\(chicken_farmer" + "@ZombieTypes" + "\\)\\s*");
        Regex regex11 = new Regex("\\s*\\(west_bull" + "@ZombieTypes" + "\\)\\s*");
        Regex regex12 = new Regex("\\s*\\(cowboy_gargantuar" + "@ZombieTypes" + "\\)\\s*");
        return new Regex("\\s*\\(west_bullrider" + "@ZombieTypes" + "\\)\\s*").replace((CharSequence) regex12.replace((CharSequence) regex11.replace((CharSequence) regex10.replace((CharSequence) regex9.replace((CharSequence) regex8.replace((CharSequence) regex7.replace((CharSequence) regex6.replace((CharSequence) regex5.replace((CharSequence) regex4.replace((CharSequence) regex3.replace((CharSequence) regex2.replace((CharSequence) regex.replace((CharSequence) this.last, "70 \\{\\{P|Cowboy Zombie|2}}"), "71 \\{\\{P|Conehead Cowboy|2}}"), "72 \\{\\{P|Buckethead Cowboy|2}}"), "73 \\{\\{P|Cart-Head Zombie|2}}"), "76 \\{\\{P|Prospector Zombie|2}}"), "77 \\{\\{P|Pianist Zombie|2}}"), "80 \\{\\{P|Vegan Zombie|2}}"), "81 \\{\\{P|Poncho Zombie|2}}"), "81 \\{\\{P|Poncho Zombie|2}}"), "79 \\{\\{P|Chicken Wrangler Zombie|2}}"), "78 \\{\\{P|Zombie Bull|2}}"), "74 \\{\\{P|Wild West Gargantuar|2}}"), "75 \\{\\{P|Zombie Bull Rider|2}}");
    }
}
